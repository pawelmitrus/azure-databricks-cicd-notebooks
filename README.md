* test notebooks
    * each notebook uses `dbutils.widgets` to get parameters and `dbutils.notebook.exit` to return status
    * notebooks should remain small if possible, so tests are more meaningful
    * tests are organized with separate notebooks (scala, so the notebook context path can be get), `_master_test` notebook orchestrate tests\
* development
    * each developer works on separate feature branches
    * developer via databricks-cli import/export notebooks to private location on Databricks workspace
    * changes are commited on local machine
* CI (Azure DevOps)
    * `azure_pipeline_run_tests` pipeline should be set to validate pull request to the master branch
    * master branch policy doesn't allow pushes to master branch (only via pull request)
* CD (Azure DevOps)
    * `azure_pipeline_publish_artifact` will be triggered any time new release/* branch is created
    * release pipeline should use build artifact ftom above pipeline as a source
    * release pipeline can consist 2 steps - staging and production
        * staging - triggered with release/* branch creation, uses notebooks from published artifact and deploy them to staging folder
        * production - deployed manually, deploy notebooks to production folder