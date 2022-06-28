library(shiny)
library(shinyWidgets)
library(tidyverse)
library(plotly)

ui <- fluidPage(
  
  titlePanel("Search Employee Database"),
  h5("The Data in this report is fictitious, pls no report"),
  
  sidebarLayout(
    sidebarPanel(
      
      uiOutput("picker"),
      actionButton("view", "View Selection"),
      p('___'),
      textInput('name', 'Enter Employee ID', "VAuq292"),
      p('___'),
      h4('Worst Employees Today'),
      tableOutput("worst_table"),
      p('___'),
      textAreaInput('email',
                    "Insert email text",
                    "This is a warning...", rows = 5),
      actionButton("button",
                   "Fire incompetent employees!",
      ),
      
    ),
    
    mainPanel(
      actionButton("runfile",
                   "Add day to data",
      ),
      h2('Employee Explorer'),
      h4("Productivity Over Time"),
      plotOutput('trend'),
      h4("Employee Database"),
      DT::dataTableOutput("table"),
    )
  )
)

library(shiny)
library(DT)
library(tidyverse)

server <- function(session, input, output) {
  
  df <- read_csv("people.csv")
  data <- reactive({
    df
  })
  
  output$picker <- renderUI({
    pickerInput(inputId = 'pick', 
                label = 'Choose columns for employee database', 
                choices = colnames(data()),
                options = list(`actions-box` = TRUE),multiple = T)
  })
  
  datasetInput <- eventReactive(input$view,{
    
    datasetInput <- data() %>% 
      select(input$pick)
    
    return(datasetInput)
    
  })
  
  output$table <- renderDT({datasetInput()
  })
  
  observeEvent(input$runfile, {
  output$trend <- renderPlot({

        
    read_csv("prod.csv") %>% select(input$name) %>% mutate(count = .[[1]], index = row_number()) %>% 
      ggplot(aes(x = index, y = count)) +
      geom_line(size = 2) +
      theme_classic() +
      labs(x = "Recorded days",
           y = 'Productivity Score')
  })
  })
  observeEvent(input$runfile, {
  
  output$worst_table <- renderTable({
    read_csv("prod.csv") |> 
      tail(1) |> 
      mutate(row = row_number()) |> 
      pivot_longer(cols = !row,  names_to = "worker_id", values_to = "productivity") |> 
      arrange(productivity) |> 
      head(10) |> 
      left_join(
        (read_csv("people.csv") |> select(worker_id, name))
      ) |> select(-row)
  })
  })
  
  observeEvent(input$button, {
    session$sendCustomMessage(type = 'testmessage',
                              message = 'Thank you for clicking')
  })
  
  
  observeEvent(input$runfile, {
    reticulate::py_run_file("update_prod.py")
    # reticulate::py_run_file("automation.py")
  })
  
}


# Run the application 
shinyApp(ui = ui, server = server)
