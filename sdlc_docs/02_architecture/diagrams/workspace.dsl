workspace "Gaussian Explorer Architecture" "Canonical C4 model for architecture version 1.0 and source story version 1.0." {
    model {
        researcher = person "Researcher" "Uploads small experimental datasets, configures Gaussian Process Regression, interprets uncertainty, and exports results."

        localFileSystem = softwareSystem "Researcher's Local File System" "Source of uploaded CSV files and destination for downloaded result, plot, and metadata artifacts." {
            tags "External"
        }

        gaussianExplorer = softwareSystem "Gaussian Process Regression Web Application" "Streamlit application for in-memory Gaussian Process Regression analysis of uploaded CSV data." {
            streamlitApp = container "Streamlit Web Application" "Provides the interactive workflow, validates inputs, fits the model, visualizes uncertainty, and creates exports." "Python 3.12, Streamlit" {
                workflowUi = component "Workflow UI" "Presents upload, variable selection, settings, fit, visualization, and export controls."
                csvValidation = component "CSV parsing and validation" "Parses uploaded CSV data and rejects unsupported, malformed, oversized, or structurally unusable input."
                settingsPreparation = component "Variable and GPR settings" "Derives numeric variables, records selected X/Y columns, and prepares editable GPR settings."
                gprFitting = component "GPR fitting and prediction" "Fits Gaussian Process Regression and computes predicted mean and uncertainty bounds."
                visualization = component "Prediction and uncertainty visualization" "Renders original data, predicted curve, and uncertainty estimates for interpretation."
                exportGeneration = component "Export generation" "Builds result CSV, plot output, and reproducibility metadata from the active analysis state."
            }

            analysisSession = container "In-memory Analysis Session" "Ephemeral active-session state for uploaded data, selected variables, settings, prediction results, visualization metadata, and export payloads." "Streamlit session state, Python objects"
        }

        researcher -> streamlitApp "Uses to run an analysis"
        researcher -> workflowUi "Interacts with the analysis workflow"
        researcher -> localFileSystem "Selects CSV files from and saves downloaded artifacts to"
        localFileSystem -> streamlitApp "Provides uploaded CSV content"
        streamlitApp -> localFileSystem "Provides downloaded results, plot, and metadata"

        workflowUi -> csvValidation "Submits uploaded CSV content for validation"
        csvValidation -> analysisSession "Stores accepted dataset"
        workflowUi -> settingsPreparation "Submits variable choices and model settings"
        settingsPreparation -> analysisSession "Stores selected variables and settings"
        workflowUi -> gprFitting "Requests model fitting for valid analysis inputs"
        gprFitting -> analysisSession "Reads analysis inputs and stores prediction results"
        workflowUi -> visualization "Requests prediction and uncertainty chart"
        visualization -> analysisSession "Reads dataset and prediction results"
        workflowUi -> exportGeneration "Requests result, plot, and metadata exports"
        exportGeneration -> analysisSession "Reads fitted analysis state and stores generated export payloads"

        deploymentEnvironment "LocalDeployment" {
            deploymentNode "User-accessible Python Runtime" "Local workstation, lab server, or simple app host" "Python 3.12+" {
                deploymentNode "Streamlit Process" "Streamlit server process" "Streamlit" {
                    containerInstance streamlitApp
                    containerInstance analysisSession
                }
            }
        }
    }

    views {
        systemContext gaussianExplorer "SystemContext" {
            title "System Context - Gaussian Process Regression Web Application"
            description "Shows the researcher, the application, and the local file-system boundary for uploads and downloads."
            include *
            autoLayout lr
        }

        container gaussianExplorer "Containers" {
            title "Containers - Gaussian Process Regression Web Application"
            description "Shows the single Streamlit runtime container and its ephemeral in-memory analysis state."
            include *
            autoLayout lr
        }

        component streamlitApp "StreamlitComponents" {
            title "Components - Streamlit Web Application"
            description "Shows the internal responsibilities owned by the Streamlit application container."
            include *
            autoLayout lr
        }

        dynamic streamlitApp "MainAnalysisFlow" {
            title "Dynamic - Main Analysis Flow"
            description "Shows the primary upload, selection, fitting, visualization, and export interaction sequence."
            researcher -> workflowUi "Uploads CSV"
            workflowUi -> csvValidation "Parses and validates upload"
            csvValidation -> analysisSession "Stores accepted dataset"
            researcher -> workflowUi "Selects variables and GPR settings"
            workflowUi -> settingsPreparation "Validates choices and settings"
            settingsPreparation -> analysisSession "Stores analysis inputs"
            researcher -> workflowUi "Fits model"
            workflowUi -> gprFitting "Requests GPR fit and prediction"
            gprFitting -> analysisSession "Stores prediction results"
            workflowUi -> visualization "Renders visualization"
            researcher -> workflowUi "Requests exports"
            workflowUi -> exportGeneration "Builds export artifacts"
            autoLayout lr
        }

        deployment gaussianExplorer "LocalDeployment" "LocalDeployment" {
            title "Deployment - Local or Single-Process Streamlit Runtime"
            description "Shows the MVP deployment assumption: one Streamlit process with in-process session state."
            include *
            autoLayout lr
        }

        styles {
            element "Person" {
                shape person
                background #0b5f6a
                color #ffffff
            }
            element "Software System" {
                background #345995
                color #ffffff
            }
            element "Container" {
                background #4f7cac
                color #ffffff
            }
            element "Component" {
                background #9ec5ab
                color #000000
            }
            element "External" {
                background #6d6d6d
                color #ffffff
            }
        }
    }
}
