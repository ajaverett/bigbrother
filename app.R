# library(rsconnect)
# rsconnect::deployApp('path/to/your/app')


library(shiny)
library(tidyverse)
library(DT)



# ui <- fluidPage(
#   titlePanel("Employee Explorer (this is fake data please do not report us)"),
#       column(12,DTOutput('table'))
# )

ui <- fluidPage(
  titlePanel("Employee Explorer (this is fake data please do not report us)"),
  sidebarLayout(
    sidebarPanel(
      selectInput("df.columns", "Select columns to display", names(df), multiple = TRUE),
    ),
    mainPanel(
      column(12,DTOutput('table'))
    )
  )
)


server <- function(input, output) {
  
  df <- read_csv("people.csv",
                 #col_names = F,
  )

  
  colname_vector <- c("worker_id","name","age","productivity")

  observe(input$df.columns, {
    
    if (!is.null(input$df.columns)){
      
      colname_vector <- c("worker_id","name","age","productivity")
      print("1a------")
      print(input$df.columns)
      print("2------")
      print(colname_vector)
      print("3------")
      
    } else {
      
      colname_vector <- (input$df.columns)
    }
  })
  
  
  # temp()
  
    output$table <- renderDT(df |> select(colname_vector),
                             filter = "top",
                             options = list(
                               pageLength = 5
                             ))
  
  
  
  
  
}



shinyApp(ui = ui, server = server)

