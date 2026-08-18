class LlmPromptInjectionJailbreakFirewallClient:
    def inspect_prompt(self, user_input_prompt: str, strict_mode: bool = True) -> dict:
        dangerous_patterns = ["ignore previous instructions", "system prompt", "dan mode", "base64 decode"]
        lower = user_input_prompt.lower()
        threat = "NONE"
        safe = True
        for p in dangerous_patterns:
            if p in lower:
                safe = False
                threat = "PROMPT_INJECTION_OVERRIDE_ATTEMPT"
                break
        return {
            "is_safe": safe,
            "threat_type": threat,
            "sanitized_prompt": user_input_prompt if safe else "[SANITIZED_PROMPT_BLOCKED]",
            "latency_ms": 3
        }
