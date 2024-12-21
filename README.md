# Code documentation generator 

An experimentation to see how well free-tier LLM can generate a documentation doc in markdown format for any project structure (currently only for clojure projects). 

This repository only contains the code bundler, which bundle the code and used as a prompt to generate the documentation. The documentation in `docs/` and the bundler is generated using Gemini 1.5 flash model.