# Code documentation generator 

```
An experimentation to see how well free-tier LLM can generate a documentation in markdown format for 
any project structure (currently only for clojure projects). 

This repository only contains the code bundler, which bundle the code and used as a prompt to generate 
the documentation. The web version of the Gemini 1.5 model and Open AI is not able to give file, so
the output format will be in json and then ask the model to make a script to convert it to markdown.

FAQ:
> Why not use the API of the model?
too lazy (and broke) for that

> Why not use the model locally?
same answer
```