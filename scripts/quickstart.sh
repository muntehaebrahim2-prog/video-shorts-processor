#!/bin/bash
# Quick start script for running all examples

echo "========================================"
echo "Video Shorts Processor - Quick Start"
echo "========================================"
echo ""

# Check Python installation
if ! command -v python &> /dev/null; then
    echo "Error: Python is not installed"
    exit 1
fi

# Activate virtual environment
if [[ "$VIRTUAL_ENV" == "" ]]; then
    if [ -f "venv/bin/activate" ]; then
        source venv/bin/activate
    elif [ -f "venv/Scripts/activate" ]; then
        source venv/Scripts/activate
    fi
fi

# Menu
while true; do
    echo ""
    echo "Select an example to run:"
    echo "1. Generate sample test videos"
    echo "2. Process single video with trimming"
    echo "3. Batch process multiple videos"
    echo "4. Process and upload to YouTube"
    echo "5. Parallel video processing"
    echo "6. Custom video editing"
    echo "0. Exit"
    echo ""
    read -p "Enter choice [0-6]: " choice

    case $choice in
        1)
            echo "Running: Generate sample test videos..."
            python examples/example5_generate_test_videos.py
            ;;
        2)
            echo "Running: Single video processing..."
            python examples/example1_single_video.py
            ;;
        3)
            echo "Running: Batch video processing..."
            python examples/example2_batch_processing.py
            ;;
        4)
            echo "Running: Process and upload to YouTube..."
            python examples/example3_process_and_upload.py
            ;;
        5)
            echo "Running: Parallel video processing..."
            python examples/example4_parallel_processing.py
            ;;
        6)
            echo "Running: Custom video editing..."
            python examples/example6_custom_editing.py
            ;;
        0)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid choice. Please try again."
            ;;
    esac
done
