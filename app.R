
library(shiny)
library(tidyverse)

df <- read_csv("people.csv",
               #col_names = F,
               )

ui <- fluidPage(
  titlePanel("Employee Explorer"),
  
  #fluidRow(
    column(12,
           DTOutput('table')
    )
  #)
)

# ui <- fluidPage(
#   titlePanel("Employee Explorer"),
#   sidebarLayout(
#     sidebarPanel(textInput('name', 'Enter Name', 'David')),
#     mainPanel(plotOutput('trend'))
#   )
# )

server <- function(input, output) {
    output$table <- renderDT(df,
                             filter = "top",
                             options = list(
                               pageLength = 5
                             )
    )
  }

shinyApp(ui = ui, server = server)

