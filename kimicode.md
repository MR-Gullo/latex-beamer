To set up your terminal so that you can run Claude Code with Kimi K2 via Groq as the provider, using an OpenRouter API key, and invoke it with `kimiyolo` including the `--dangerously-skip-permissions` argument, we can leverage OpenRouter's unified API. OpenRouter acts as a proxy that supports multiple AI models (including Groq and Kimi K2) through a single endpoint, as detailed in the OpenRouter Quickstart Guide (openrouter.ai/docs). Here's how to configure it step-by-step, considering the current date and time (11:37 AM EDT, Thursday, July 17, 2025) and the latest trends in API integration.

---

### Prerequisites

1. **API Key**:

   - Obtain an OpenRouter API key from openrouter.ai. This key will authenticate requests to access Groq and Kimi K2 models.
   - No separate Groq or Kimi API keys are needed since OpenRouter handles model access.

2. **Tools**:

   - Install Claude Code (follow instructions at github.com/anthropics/claude-code).
   - Ensure you have a Unix-like shell (e.g., Bash, Zsh) and a text editor (e.g., `nano`, `vim`).

3. **Understanding Risks**:

   - The `--dangerously-skip-permissions` flag bypasses security checks, which can be dangerous. Use it only in a controlled, isolated environment (e.g., a devcontainer or virtual machine).

---

### Step-by-Step Setup

#### 1. Configure Environment Variables

OpenRouter uses a single endpoint (`https://openrouter.ai/api/v1`) and authenticates via an API key in the `Authorization` header. Modify your shell configuration file (e.g., `.bashrc` or `.zshrc`) to set the necessary variables:

```bash
# Add to ~/.bashrc or ~/.zshrc
export OPENROUTER_API_KEY="or-sk-YOUR-OPENROUTER-API-KEY"
export ANTHROPIC_BASE_URL="https://openrouter.ai/api/v1"
export ANTHROPIC_AUTH_TOKEN="$OPENROUTER_API_KEY"
export ANTHROPIC_MODEL="moonshotai/kimi-k2"  # Specify Kimi K2 as the model
```

- Replace `or-sk-YOUR-OPENROUTER-API-KEY` with your actual OpenRouter API key.
- Here is my API KEY from open router: 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
-
- The `ANTHROPIC_BASE_URL` is set to OpenRouter's endpoint, and `ANTHROPIC_MODEL` specifies Kimi K2, which is supported via OpenRouter (see openrouter.ai/models).
- OpenRouter automatically routes the request to Groq's infrastructure if Kimi K2 is hosted there, leveraging Groq's recent integration trends (noted in X posts from July 16, 2025).

Apply the changes:

```bash
source ~/.bashrc  # or source ~/.zshrc
```

#### 2. Create a Custom Shell Function

To run Claude Code with this setup by typing `kimiyolo`, define a custom function in your shell configuration file. Add the following:

```bash
# Add to ~/.bashrc or ~/.zshrc
kimiyolo() {
  # Ensure OpenRouter is used with Kimi K2
  export ANTHROPIC_BASE_URL="https://openrouter.ai/api/v1"
  export ANTHROPIC_AUTH_TOKEN="$OPENROUTER_API_KEY"
  export ANTHROPIC_MODEL="moonshotai/kimi-k2"

  # Run Claude Code with the dangerously-skip-permissions flag
  claude --dangerously-skip-permissions "$@"

  # Optional: Restore original environment (if you switch back to another setup)
  # export ANTHROPIC_BASE_URL="https://api.moonshot.ai/anthropic"
  # export ANTHROPIC_AUTH_TOKEN="$KIMI_API_KEY"  # Uncomment if needed
}
```

- The function sets the environment to use OpenRouter with Kimi K2, then calls `claude` with the `--dangerously-skip-permissions` flag and any additional arguments (`$@`).
- The restoration step is commented out since you're primarily using OpenRouter, but you can uncomment it if you switch back to a direct Kimi setup.

Apply the changes:

```bash
source ~/.bashrc  # or source ~/.zshrc
```

#### 3. Test the Setup

- Open a new terminal or run `source ~/.bashrc` (or `.zshrc`).
- Type `kimiyolo` and press Enter. If configured correctly, it should launch Claude Code, routing through OpenRouter to Kimi K2 on Groq's infrastructure, skipping permissions checks.
- To pass a prompt or command, use `kimiyolo -c "your prompt here"` (e.g., `kimiyolo -c "generate a bash script"`).

#### 4. Troubleshooting

- **Model Not Found**: Ensure `moonshotai/kimi-k2` is supported by OpenRouter. Check the latest model list at openrouter.ai/models (updated as of July 2025).
- **Authentication Errors**: Verify your OpenRouter API key. If issues persist, regenerate the key and update the environment variable.
- **Permission Issues**: The `--dangerously-skip-permissions` flag might not work if Claude Code enforces strict checks. Test in a devcontainer or consult github.com/anthropics/claude-code/issues for updates.
- **Performance**: OpenRouter's fallback mechanism might switch to another provider if Groq is unavailable. Monitor logs or add `export OPENROUTER_FORCE_MODEL="moonshotai/kimi-k2"` to enforce Kimi K2.

---

### Additional Notes

- **Security**: The `--dangerously-skip-permissions` flag poses risks (e.g., unintended system access). Use it only in a sandboxed environment, especially with OpenRouter, which aggregates multiple APIs.
- **Cost**: OpenRouter bills based on usage (see openrouter.ai/pricing). Monitor your API key's credit limit to avoid surprises.
- **Latest Trends**: The July 16, 2025, X post by @taf2 and the OpenAI-Google Cloud partnership (Reuters, July 16, 2025) indicate a surge in cross-provider integrations, making OpenRouter a viable choice for this setup.

This configuration aligns with the community hacks from the X thread and leverages OpenRouter's flexibility. Let me know if you need further assistance or encounter specific errors!
