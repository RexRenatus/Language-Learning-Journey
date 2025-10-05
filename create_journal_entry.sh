#!/bin/bash

# Journal Entry Creator Script
# This script automatically creates a new journal entry based on existing template patterns

# Set script directory and journal entries directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
JOURNAL_DIR="$SCRIPT_DIR/Journal_Entries"

# Function to get current date in YYYYMMDD format
get_date() {
    if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
        # Windows/Git Bash
        date +"%Y%m%d"
    else
        # Unix/Linux/macOS
        date +"%Y%m%d"
    fi
}

# Function to get year and month for directory structure
get_year() {
    if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
        date +"%Y"
    else
        date +"%Y"
    fi
}

get_month() {
    if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
        date +"%m"
    else
        date +"%m"
    fi
}

# Function to create directory structure
create_directories() {
    local year=$(get_year)
    local month=$(get_month)
    local target_dir="$JOURNAL_DIR/$year/$month"
    
    if [ ! -d "$target_dir" ]; then
        echo "Creating directory structure: $target_dir"
        mkdir -p "$target_dir"
    fi
    
    echo "$target_dir"
}

# Function to check if journal entry already exists
entry_exists() {
    local date_str=$1
    local year=$(echo $date_str | cut -c1-4)
    local month=$(echo $date_str | cut -c5-6)
    local entry_path="$JOURNAL_DIR/$year/$month/$date_str.md"
    
    if [ -f "$entry_path" ]; then
        return 0  # exists
    else
        return 1  # doesn't exist
    fi
}

# Function to get previous TODO items from most recent journal entry
get_previous_todos() {
    # Find the most recent journal entry
    local latest_entry=""
    local latest_date="00000000"
    
    # Search through all journal entries to find the most recent
    find "$JOURNAL_DIR" -name "*.md" -type f 2>/dev/null | while read -r file; do
        local filename=$(basename "$file" .md)
        if [[ "$filename" > "$latest_date" ]]; then
            latest_date="$filename"
            latest_entry="$file"
        fi
    done | tail -1
    
    # Get the latest entry file
    latest_entry=$(find "$JOURNAL_DIR" -name "*.md" -type f 2>/dev/null | sort | tail -1)
    
    if [ -n "$latest_entry" ] && [ -f "$latest_entry" ]; then
        echo "# Previous TODO Items (from $(basename "$latest_entry" .md))"
        echo ""
        
        # Extract TODO items from the most recent entry
        local in_todo_section=false
        local in_future_todo=false
        
        while IFS= read -r line; do
            if [[ "$line" =~ ^#[[:space:]]*TODO[[:space:]]*List ]]; then
                in_todo_section=true
                in_future_todo=false
                continue
            elif [[ "$line" =~ ^#[[:space:]]*Future[[:space:]]*TODO[[:space:]]*List ]]; then
                in_todo_section=false
                in_future_todo=true
                continue
            elif [[ "$line" =~ ^# ]]; then
                in_todo_section=false
                in_future_todo=false
                continue
            fi
            
            if [[ "$in_todo_section" == true ]] || [[ "$in_future_todo" == true ]]; then
                if [[ -n "$line" ]] && [[ ! "$line" =~ ^[[:space:]]*$ ]]; then
                    # Remove completion status markers and keep the task
                    local clean_line=$(echo "$line" | sed 's/(Completed)//' | sed 's/(In Progress)//' | sed 's/^[[:space:]]*//')
                    if [[ -n "$clean_line" && "$clean_line" != "-" ]]; then
                        echo "$clean_line"
                    fi
                fi
            fi
        done < "$latest_entry"
        
        echo ""
    else
        echo "# TODO List"
        echo ""
        echo "- Add your tasks here"
        echo ""
    fi
}

# Function to create journal template
create_journal_template() {
    local date_str=$1
    
    cat << EOF
# TODO List

$(get_previous_todos)

# Journal Entries

- 

# Reflection

- 

# Future TODO List

- 

EOF
}

# Function to create journal entry with optional custom date
create_entry() {
    local custom_date=""
    
    # Check if a custom date was provided as argument
    if [ $# -eq 1 ]; then
        if [[ "$1" =~ ^[0-9]{8}$ ]]; then
            custom_date="$1"
        else
            echo "Error: Date must be in YYYYMMDD format (e.g., 20251005)"
            exit 1
        fi
    fi
    
    # Use custom date or current date
    local date_str
    if [ -n "$custom_date" ]; then
        date_str="$custom_date"
    else
        date_str=$(get_date)
    fi
    
    # Check if entry already exists
    if entry_exists "$date_str"; then
        echo "Journal entry for $date_str already exists!"
        echo "Location: $JOURNAL_DIR/$(echo $date_str | cut -c1-4)/$(echo $date_str | cut -c5-6)/$date_str.md"
        read -p "Do you want to open it for editing? (y/n): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            local year=$(echo $date_str | cut -c1-4)
            local month=$(echo $date_str | cut -c5-6)
            local entry_path="$JOURNAL_DIR/$year/$month/$date_str.md"
            
            # Try to open with various editors
            if command -v code &> /dev/null; then
                code "$entry_path"
            elif command -v notepad &> /dev/null; then
                notepad "$entry_path"
            elif command -v nano &> /dev/null; then
                nano "$entry_path"
            elif command -v vim &> /dev/null; then
                vim "$entry_path"
            else
                echo "Entry location: $entry_path"
            fi
        fi
        return 0
    fi
    
    # Create directory structure
    local target_dir=$(create_directories)
    local entry_path="$target_dir/$date_str.md"
    
    # Create the journal entry
    echo "Creating journal entry for $date_str..."
    create_journal_template "$date_str" > "$entry_path"
    
    echo "Journal entry created successfully!"
    echo "Location: $entry_path"
    
    # Ask if user wants to open the file
    read -p "Do you want to open the journal entry now? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        # Try to open with various editors
        if command -v code &> /dev/null; then
            code "$entry_path"
        elif command -v notepad &> /dev/null; then
            notepad "$entry_path"
        elif command -v nano &> /dev/null; then
            nano "$entry_path"
        elif command -v vim &> /dev/null; then
            vim "$entry_path"
        else
            echo "Please open: $entry_path"
        fi
    fi
}

# Function to display usage information
show_usage() {
    echo "Usage: $0 [YYYYMMDD]"
    echo ""
    echo "Creates a new journal entry based on existing template patterns."
    echo ""
    echo "Examples:"
    echo "  $0              # Create entry for today"
    echo "  $0 20251205     # Create entry for December 5, 2025"
    echo ""
    echo "The script will:"
    echo "  - Create the necessary directory structure (YYYY/MM/)"
    echo "  - Generate a journal entry with TODO items from the most recent entry"
    echo "  - Include standard sections: TODO List, Journal Entries, Reflection, Future TODO List"
    echo "  - Check if an entry already exists and offer to open it"
}

# Main script execution
main() {
    # Check for help flag
    if [[ "$1" == "-h" || "$1" == "--help" ]]; then
        show_usage
        exit 0
    fi
    
    # Ensure journal directory exists
    if [ ! -d "$JOURNAL_DIR" ]; then
        echo "Creating Journal_Entries directory..."
        mkdir -p "$JOURNAL_DIR"
    fi
    
    echo "Journal Entry Creator"
    echo "===================="
    
    # Create the journal entry
    create_entry "$@"
}

# Run the main function with all arguments
main "$@"