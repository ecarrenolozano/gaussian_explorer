workspace "Project Architecture" "Canonical C4 architecture model" {
    model {
        user = person "User" "A person who uses the software system."

        softwareSystem = softwareSystem "Software System" "The software system being designed." {
            application = container "Application" "Provides the main application behavior." "Technology to be confirmed" {
                userInterface = component "User Interface" "Accepts user input and presents output."
                mainComponent = component "Main Component" "Provides a cohesive application responsibility."
            }

            database = container "Database" "Stores application data." "Database technology to be confirmed"
        }

        user -> application "Uses"
        user -> userInterface "Interacts with"
        userInterface -> mainComponent "Delegates work to"
        mainComponent -> database "Reads from and writes to"

        deploymentEnvironment "Local" {
            deploymentNode "Runtime Environment" "Execution environment for the software system." "Technology to be confirmed" {
                containerInstance application
                containerInstance database
            }
        }
    }

    views {
        systemContext softwareSystem "SystemContext" {
            include *
            autoLayout lr
        }

        container softwareSystem "Containers" {
            include *
            autoLayout lr
        }

        component application "ApplicationComponents" {
            include *
            autoLayout lr
        }

        dynamic application "MainFlow" {
            title "Dynamic - Main Flow"
            user -> userInterface "Starts workflow"
            userInterface -> mainComponent "Delegates work"
            mainComponent -> database "Reads from and writes to"
            autoLayout lr
        }

        deployment softwareSystem "Local" "LocalDeployment" {
            title "Deployment - Local Runtime"
            include *
            autoLayout lr
        }

        styles {
            element "Person" {
                shape person
            }
            element "Software System" {
                background #1168bd
                color #ffffff
            }
            element "Container" {
                background #438dd5
                color #ffffff
            }
            element "Component" {
                background #85bbf0
                color #000000
            }
        }
    }
}
