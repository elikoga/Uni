#!/usr/bin/env bash

# Buffer to store input
BUFFER=""

# Function to flush buffer
flush_buffer() {
    echo "flushing buffer" >&2
    echo -n "$BUFFER"
    BUFFER=""
}

# Function to clean up
cleanup() {
    echo "script shutting down" >&2
    flush_buffer
    # Clean up any persistent state
}

# Register cleanup function
trap cleanup EXIT

# Register flush_buffer function for SIGUSR1
trap flush_buffer USR1

# Read from stdin
while read -r line; do
    BUFFER+="$line"$'\n'
done
