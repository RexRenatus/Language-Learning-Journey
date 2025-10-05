@echo off
setlocal enabledelayedexpansion

:: Journal Entry Creator Batch Script
:: This script automatically creates a new journal entry based on existing template patterns

:: Set script directory and journal entries directory
set "SCRIPT_DIR=%~dp0"
set "JOURNAL_DIR=%SCRIPT_DIR%Journal_Entries"

:: Function to get current date in YYYYMMDD format
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YYYY=%dt:~0,4%"
set "MM=%dt:~4,2%"
set "DD=%dt:~6,2%"
set "CURRENT_DATE=%YYYY%%MM%%DD%"

:: Check if custom date was provided as argument
set "USE_DATE=%CURRENT_DATE%"
if not "%~1"=="" (
    if "%~1"=="--help" (
        goto :show_usage
    ) else if "%~1"=="-h" (
        goto :show_usage
    ) else (
        echo %~1| findstr /r "^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$" >nul
        if !errorlevel! equ 0 (
            set "USE_DATE=%~1"
        ) else (
            echo Error: Date must be in YYYYMMDD format (e.g., 20251005)
            exit /b 1
        )
    )
)

:: Extract year and month from date
set "ENTRY_YEAR=%USE_DATE:~0,4%"
set "ENTRY_MONTH=%USE_DATE:~4,2%"
set "TARGET_DIR=%JOURNAL_DIR%\%ENTRY_YEAR%\%ENTRY_MONTH%"
set "ENTRY_PATH=%TARGET_DIR%\%USE_DATE%.md"

echo Journal Entry Creator
echo ====================
echo.

:: Check if entry already exists
if exist "%ENTRY_PATH%" (
    echo Journal entry for %USE_DATE% already exists!
    echo Location: %ENTRY_PATH%
    set /p "OPEN_EXISTING=Do you want to open it for editing? (y/n): "
    if /i "!OPEN_EXISTING!"=="y" (
        if exist "%ProgramFiles%\Microsoft VS Code\Code.exe" (
            "%ProgramFiles%\Microsoft VS Code\Code.exe" "%ENTRY_PATH%"
        ) else if exist "%ProgramFiles(x86)%\Microsoft VS Code\Code.exe" (
            "%ProgramFiles(x86)%\Microsoft VS Code\Code.exe" "%ENTRY_PATH%"
        ) else (
            notepad "%ENTRY_PATH%"
        )
    )
    goto :end
)

:: Create directory structure if it doesn't exist
if not exist "%TARGET_DIR%" (
    echo Creating directory structure: %TARGET_DIR%
    mkdir "%TARGET_DIR%" 2>nul
)


:: Create the journal entry
echo Creating journal entry for %USE_DATE%...

:: Write the simple journal template
(
echo # TODO List
echo.
echo - 
echo.
echo # Journal Entries
echo.
echo - 
echo.
echo # Reflection
echo.
echo - 
echo.
echo # Future TODO List
echo.
echo - 
echo.
) > "%ENTRY_PATH%"

echo Journal entry created successfully!
echo Location: %ENTRY_PATH%
echo.

:: Ask if user wants to open the file
set /p "OPEN_NEW=Do you want to open the journal entry now? (y/n): "
if /i "!OPEN_NEW!"=="y" (
    if exist "%ProgramFiles%\Microsoft VS Code\Code.exe" (
        "%ProgramFiles%\Microsoft VS Code\Code.exe" "%ENTRY_PATH%"
    ) else if exist "%ProgramFiles(x86)%\Microsoft VS Code\Code.exe" (
        "%ProgramFiles(x86)%\Microsoft VS Code\Code.exe" "%ENTRY_PATH%"
    ) else (
        notepad "%ENTRY_PATH%"
    )
)

goto :end


:: Function to display usage information
:show_usage
echo Usage: %~nx0 [YYYYMMDD]
echo.
echo Creates a new journal entry with a simple template skeleton.
echo.
echo Examples:
echo   %~nx0              # Create entry for today
echo   %~nx0 20251205     # Create entry for December 5, 2025
echo.
echo The script will:
echo   - Create the necessary directory structure (YYYY\MM\)
echo   - Generate a journal entry with empty template sections
echo   - Include standard sections: TODO List, Journal Entries, Reflection, Future TODO List
echo   - Check if an entry already exists and offer to open it
echo.
echo Current date: %CURRENT_DATE%
goto :end

:end
echo.
pause