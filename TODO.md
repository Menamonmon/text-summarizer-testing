- Add spacy to azure testing & use it to filter unecessary text which includes:
  - Questions
  - Titles and Headers
  - Indentation and Spaces between paragraphs
  - All other sentence units that don't end with "." or ";".