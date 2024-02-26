# Semantic Synth
So you've decided to build out a RAG (Retrieval Augmented Generation) tool. Great! Now you want to build a vector search index for a critical production task. 

Before you push into prodcution though, you'd like to be able to test how well the search index itself is working.

We have also released a 520k sample dataset for you to run tests. Access at: [Huggingface Hub](https://huggingface.co/datasets/wordlabs/semantic_search_quality)

## Current methods for testing
Having reviewed multiple different platforms that work on semantic search correctness, the primary idea is to collect some passage from the dataset, and generate questions on it using an LLM, then get the LLM to answer it, and generate different types of metrics, such as faithfulness, correctness, etc. 

This is an expensive operation owing to the multiple LLM calls, not to mention would not be conducive for very large scale data testing or continous monitoring. 

## How does this package work?
Given any text, we generate keywords using YAKE library. This effectively makes the test self supervised, without need for expensive 

### Philosophy
Semantic search mainly works on finding different latent meanings between queries and vectors in a search index. Therefore, it only makes sense that it should be highly effective at finding passages that contain key phrases in a document

However, there are multiple steps of possible loss. First is the chunking strategy. Then comes your vector embedding model. Post which comes the capability of the vector index you are using (these indices are often based on approximation algorithms and can be quite lossy)

For academic purposes, premade datasets are good enough, but how do you run these estimates on your own data? That is where Semantic Synth comes in

if a vector search index works well, it will be able to find phrases in your passages effectively. If not, maybe there's more to look at, such as your chunking strategy, or your embedding model itself

### Who is this package for?
This package is specifically for testing the retrieval capacity of your vector search index, for testing statistical metrics such as precision, recall, F1 scores, etc.

Currently we support the generation of synthetic search terms for your content so that you can perform search and calculate accuracy metrics. We are working on adding a full fledged testing suite. 

### Why did we build this?
This package was built to perform research on how different chunking strategies affect vector search accuracy.

## Usage

> WARNING: Please note that this is an alpha release and is only suitable for testing, not for production

