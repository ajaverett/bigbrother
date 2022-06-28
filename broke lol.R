library(shiny)
library(shinyWidgets)
library(tidyverse)

ui <- fluidPage(
  
  # Application title
  titlePanel("Search Employee Database"),
  h5("The Data in this report is fictitious, pls no report"),
  
  # Sidebar with a slider input for number of bins 
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
                   "Send warning to worst employees today by email",
                   ),
      
    ),
    
    # Show a plot of the generated distribution
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
  
  df <- read_csv("https://raw.githubusercontent.com/ajaverett/bigbrother/main/people.csv")
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
  
  output$trend <- renderPlot({
    # CODE BELOW: Update to display a line plot of the input name
    
    read_csv("https://raw.githubusercontent.com/ajaverett/bigbrother/main/prod.csv") %>% select(input$name) %>% mutate(count = .[[1]], index = row_number()) %>% 
      ggplot(aes(x = index, y = count)) +
      geom_line(size = 2) +
      theme_classic() +
      labs(x = "Recorded days",
           y = 'Productivity Score')
  })
  
  output$worst_table <- renderTable({
    read_csv("https://raw.githubusercontent.com/ajaverett/bigbrother/main/prod.csv") |> 
      tail(1) |> 
      mutate(row = row_number()) |> 
      pivot_longer(cols = !row,  names_to = "worker_id", values_to = "productivity") |> 
      arrange(productivity) |> 
      head(10) |> 
      left_join(
        (read_csv("https://raw.githubusercontent.com/ajaverett/bigbrother/main/people.csv") |> select(worker_id, name))
      ) |> select(-row)
  })
  
  observeEvent(input$button, {
    session$sendCustomMessage(type = 'testmessage',
                              message = 'Thank you for clicking')
  })
  
  
  observeEvent(input$runfile, {
    reticulate::py_run_file("update_prod.py")
  })
  
}


# Run the application 
shinyApp(ui = ui, server = server)
