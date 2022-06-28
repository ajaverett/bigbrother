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
      textInput('name', 'Enter Employee ID', "VAuq292")
      
    ),
    
    # Show a plot of the generated distribution
    mainPanel(
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
  
}


# Run the application 
shinyApp(ui = ui, server = server)
