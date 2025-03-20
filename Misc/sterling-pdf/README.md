
# How to run Stirling PDF on Local Machine 

## What is Stirling 
Stirling PDF brings you the tools you need to master PDFs, all while keeping your private information secure.
Convert to PDF: Convert a wide variety of image types to super high-quality PDFs
Convert from PDF: Convert PDFs to virtually any image type with minimal loss of resolution
Organize: Merge or split PDFs, create custom layouts, and add page numbers
View and edit: Edit annotations, embed images, and change PDF metadata
Sign and secure: Sign PDFs, add or remove passwords, and instantly redact private information


## Advanced Features: 
- Repair corrupt files, reveal hidden JavaScript, and auto-split pages
- Extensive PDF Functionality: Access 50+ tools, including signing, converting, merging, and more.
- Advanced Customization: Deep customization, themes, and environment variables.
- Enterprise Features: SSO, user management, and permission controls.
- Data Security: Local file processing with automatic deletion post-task.
- Scalability & Automation: Batch processing with Docker and Kubernetes support.
- API Integration: Use APIs for automation and external integrations.
- Open-Source: Community-driven with frequent updates and GitHub support.
- Multi-Language Support: Available in 38+ languages with active translations.

## Features in Details
1. Adjust page size/scale
1. Crop PDF
1. Extract page(s)
1. Merge
1. Multi-Page Layout
1. Organize
1. PDF Multi Tool
1. Remove
1. Rotate
1. Single Large Page
1. Split
1. Convert file to PDF
1. HTML to PDF
1. Image to PDF
1. Markdown to PDF
1. URL/Website To PDF
1. PDF to CSV
1. PDF to HTML
1. PDF to Image
1. PDF to Markdown
1. PDF to PDF/A
1. PDF to Presentation
1. PDF to RTF (Text)
1. PDF to Word
1. PDF to XML
1. Add Password
1. Add Stamp to PDF
1. Add Watermark
1. encrypted
1. Manual Redaction
1. Remove Certificate Sign
1. Remove Password
1. Sanitize
1. Sign
1. Sign with Certificate
1. Validate PDF Signature
1. Add image
1. Add Page Numbers
1. Change Metadata
1. Compare
1. Extract Images
1. Flatten
1. Get ALL Info on PDF
1. OCR / Cleanup scans
1. Remove Annotations
1. Remove Blank pages
1. Remove image
1. Replace and Invert Color
1. View/Edit PDF
1. Adjust Colors/Contrast
1. Auto Split by Size/Count
1. Auto Split Pages
1. Compress
1. Detect/Split Scanned photos
1. Overlay PDFs
1. Pipeline
1. Repair
1. Show Javascript
1. Split PDF by Chapters
1. Split PDF by Sections

## Local API 
http://localhost:8092/swagger-ui/index.html

github: https://github.com/Stirling-Tools/Stirling-PDF/blob/main/HowToUseOCR.md   
youtube: https://www.youtube.com/watch?v=o8N-njA57iQ   
docs: https://docs.stirlingpdf.com/

## How to Setup on Local Machine 
```
wsl
cd ~/projects/
mkdir stirling-pdf 
cd stirling-pdf 
```

### Docker Compose file 
docker-compose.yml
```
services:
  stirling-pdf:
    image: frooodle/s-pdf:latest
    ports:
      - '8092:8080'
    volumes:
      - ./trainingData:/usr/share/tessdata # Required for extra OCR languages
      - ./extraConfigs:/configs
#     - /location/of/customFiles:/customFiles/
#     - ./logs:/logs/
    environment:
      DOCKER_ENABLE_SECURITY: "false"
      INSTALL_BOOK_AND_ADVANCED_HTML_OPS: "false"
      LANGS: "en_US"
```

## download image
docker compose pull 

## run container
docker compose up -d && docker compose logs -f

Cancell the log : ctrl + c 

## Know the IP Address 
ip -br -4 a
 

## In the browser 
http://172.29.198.105:8092/pdf-to-html 