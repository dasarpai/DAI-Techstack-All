wsl

docker run -it --gpus all -v /mnt/d/github/2-Solutions/buransh/neo2.7b/gpt-neo-2.7B:/workspace -p 8888:8888 pytorch/pytorch:latest-jupyter


sudo apt-get install git-lfs

git lfs install

GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/EleutherAI/gpt-neo-2.7B

from the link below download only pytorch.bin model file. It will around 10GB.
https://huggingface.co/EleutherAI/gpt-neo-2.7B/tree/main

I need to download one needed model.
wget https://huggingface.co/EleutherAI/gpt-neo-2.7B/resolve/main/pytorch_model.bin

don't push this file into git.

How to use this model?

# Way 1:
```
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B")

```


# Way 2
```
# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-2.7B")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-2.7B")
```


