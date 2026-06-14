# Agent Spec Template v4.3

authority_status: canonical-agent-spec
packet_version: v4.3

```yaml
name: "<agent-name>"
agent_family: "parent-route | manager | wizard-loop | voice | auditor | child"
wave: "<Decision Council | Failure Council | Follow-Up Council | manager | any>"
tools: "<runtime-specific tool list or adapter mapping>"
source_lineage: "<source path or generated reason>"
```

Required body sections:

1. Purpose
2. Boot order
3. Inputs expected
4. Procedure
5. Output/receipt schema
6. Fail conditions / decorative noise
7. v4.3 packet adaptation note
