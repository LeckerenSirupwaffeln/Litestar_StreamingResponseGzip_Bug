#!/usr/bin/env bash  

# ensures errors have high visibility
set -o errexit 
set -o pipefail 
set -o nounset  

# starts Starlite application  
echo Starting Starlite Production App on port 8000... 
# remove --reload option when in production
uvicorn --host 0.0.0.0 --port 8000 --reload --lifespan on app.app:app