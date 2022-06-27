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
      actionButton("view", "View Selection")
      
    ),
    
    # Show a plot of the generated distribution
    mainPanel(
      h2('Employee Explorer'),
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
                label = 'Choose', 
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
}


# Run the application 
shinyApp(ui = ui, server = server)
