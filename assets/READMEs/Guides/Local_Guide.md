<div align="center">

# How to use local AI in Coditan
Before even thinking of downloading a model you must **first know what AI you'll use**
You can use the table grid below to find the best match for you :

> [!Note]
> All of the VRAM usage is calculated with the ```Q4_K_M``` quantization used by almost all models uploaded to Ollama.
> This list is a near estimate of what we expect with about a 32k context window using specific Optimization Ollama has built in

| **GPU** | **VRAM** | **Model Size** |
|---------|----------|------------------|
| Nvidia RTX 3050 | 6gb | 3 billion parameters |
| Nvidia RTX 3080 | 12gb | 7 billion parameters |
| Nvidia RTX 4070 TI Super | 16gb | 14 billion parameters |
| Nvidia RTX A4500 | 20gb | 24 billion parameters |
| Nvidia RTX A5000 | 24gb | 35 billion parameters |
| Nvidia RTX A6000 | 48gb | 72 billion parameters |


<div align="left">

# How to install & use a model
For this guide **We will use Ollama** as it provides a massive library of easy to run models and can easily be connected

- **1. Download Ollama:** To download ollama you'll need to go to **[The Official Ollama downloads](https://ollama.com/download)**
- **2. Download a Model:** After installing ollama you need to install a model, it might be confusing so we want to help you by giving a list of the best models to run!

<details>
<summary>3 billion parameters</summary>

```bash
ollama pull qwen2.5-coder:3b
```

</details>

<details>
<summary>7 billion parameters</summary>

```bash
ollama pull qwen2.5-coder:7b
```

</details>

<details>
<summary>14 billion parameters</summary>

```bash
ollama pull qwen3:14b
```

</details>

<details>
<summary>24 billion parameters</summary>

```bash
ollama pull devstral-small-2:24b
```

</details>

<details>
<summary>35 billion parameters</summary>

```bash
ollama pull qwen3.6:35b
```

</details>

<details>
<summary>72 billion parameters</summary>

```bash
ollama pull qwen2.5vl:72b
```

</details>

After installing the model you'll need to open Coditan and follow these simple steps :

- **Coditan > Settings (Right top) > Preferences > Model**
- After that simply paste like this
```model
ollama/the-model-you-choose
```

- **Example of the correct usage**
```model
ollama/qwen3.6:35b
```
>[!Tip]
>The way you write the model is very simple
> Ollama - The Provider
> Qwen3.6:35b - The model you want to use
> So it's just ```provider + model``` with a ```/```in the middle.
</div>

</div>