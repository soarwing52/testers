views.py.POST [files,dev_mode, force_create]
    if form is valid
        process_files
            for filehandle in files:
            process_file(filehandle)
                ExcelProcessor.exec()
                
        