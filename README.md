# LangGraph Hello World

A simple "Hello World" program using LangGraph to demonstrate the basics of graph-based AI workflows.

## Overview

This project contains a Jupyter notebook (`Hello_Word.ipynb`) that demonstrates:
- Creating a simple LangGraph state graph
- Defining agent states using TypedDict
- Building nodes that process and transform data
- Visualizing the graph structure
- Running the graph with sample input

## What it does

The program takes a name as input (e.g., "Bob") and transforms it into a friendly greeting message: "Bob, you are doing great learning LangGraph!"

## Requirements

```bash
pip install langgraph
```

## Usage

1. Open the `Hello_Word.ipynb` notebook
2. Run all cells in order
3. The graph will process the input and return a greeting message

## Graph Structure

The graph consists of a single "greeter" node that:
1. Takes an input message (name)
2. Appends an encouraging message
3. Returns the transformed state

## Files

- `Hello_Word.ipynb` - Main notebook with the LangGraph implementation
- `README.md` - This file

## Learning Resources

This is a beginner-friendly introduction to LangGraph concepts including:
- State management
- Node functions
- Graph compilation
- Graph visualization
