# library(rsconnect)
# rsconnect::deployApp('path/to/your/app')


library(shiny)
library(tidyverse)
library(DT)

df <- read_csv("people.csv",
               #col_names = F,
               )

ui <- fluidPage(
  titlePanel("Employee Explorer (this is fake data please do not report us)"),
  
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

