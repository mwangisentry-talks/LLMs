# Ollama Breach Forensic Investigation Guide

This is a legitimate and important security topic. Let me walk you through how to conduct a forensic investigation involving Ollama.

---

## 1. Understanding Ollama

Ollama is an open-source platform for running large language models locally. Key points for forensics:

### Architecture

- Runs LLMs locally (Llama 2, Mistral, Codellama, etc.)
- Exposes a REST API (typically port 11434)
- Model files stored in `~/.ollama/models/`
- Configuration in `~/.ollama/`
- Can be run as a service/daemon

### Common Deployment

- Local machine (development/testing)
- Internal servers (enterprise)
- Containers (Docker)
- Cloud instances

---

## 2. Potential Breach Scenarios

### Scenario A: Ollama as the Attack Vector

**How it could happen:**

- Exposed Ollama API without authentication
- Prompt injection through external inputs
- Model manipulation/poisoning
- API abuse for unauthorized inference

### Scenario B: Ollama as the Target

**How it could happen:**

- Theft of model weights (intellectual property)
- Extraction of training data (privacy violation)
- Model inversion attacks
- Unauthorized access to model API

### Scenario C: Ollama as Infrastructure

**How it could happen:**

- Using Ollama to generate malicious content
- Creating deepfakes or disinformation
- Phishing email generation at scale
- Malware/ exploits generation

---

## 3. Forensic Artifacts to Collect

### 3.1 System Artifacts

**Linux/Mac:**

```bash
# Process information
ps aux | grep ollama
ls -la /proc/<ollama_pid>/

# Network connections
netstat -tulpn | grep 11434
ss -tulpn | grep 11434
lsof -i :11434

# Open files
lsof -p <ollama_pid>

# Logs
journalctl -u ollama
/var/log/ollama.log
~/.ollama/logs/

```

**Windows:**

```powershell
# Services
Get-Service ollama

# Network
Get-NetTCPConnection -LocalPort 11434

# Processes
Get-Process -Name ollama*

# Logs
Get-EventLog -LogName Application
```

### 3.2 Ollama-Specific Artifacts

```bash
# Configuration files
ls -la ~/.ollama/
cat ~/.ollama/config.yaml

# Model files (check for unauthorized models)
ls -la ~/.ollama/models/
sha256sum ~/.ollama/models/blobs/*

# Running models
ollama list
ollama ps

# API logs (if enabled)
cat ~/.ollama/logs/api.log
```

### 3.3 Container Artifacts (if Docker used)

```bash
# Container list
docker ps -a

# Container logs
docker logs <container_id>

# Container filesystem
docker export <container_id> > ollama_container.tar

# Network settings
docker inspect <container_id>

# Environment variables
docker exec <container_id> env
```

### 3.4 Network Artifacts

** firewall logs:

```bash
# IPTables
iptables -L -v -n
journalctl -k | grep 11434

# UFW
ufw status numbered

# Cloud firewall (AWS/Azure/GCP)
# Check security groups, network ACLs, firewall rules
```

**Proxy/server logs:**

```bash
# Nginx/Apache access logs
/var/log/nginx/access.log
/var/log/apache2/access.log

# Search for Ollama API calls
grep "11434" /var/log/nginx/access.log
grep "api/generate" /var/log/nginx/access.log
grep "api/chat" /var/log/nginx/access.log
```

### 3.5 Memory & Disk Forensics

```bash
# Memory dump (if live forensics)
 LiME for Linux
 FTK Imager for Windows

# Page files
# Windows: pagefile.sys,hiberfil.sys

# Temp files
ls -la /tmp/ | grep ollama
ls -la $TEMP | grep ollama
```

---

## 4. Investigation Methodology

### Phase 1: Evidence Identification

1. **Timeline reconstruction**
   - When was Ollama installed?
   - When was it last updated?
   - When did suspicious activity start?

2. **Scope determination**
   - Which systems had Ollama?
   - Who had access?
   - What models were loaded?

3. **Attack surface analysis**
   - Was API exposed to network?
   - Was authentication enabled?
   - Were there any known vulnerabilities?

### Phase 2: Evidence Collection

**Order of volatility (collect in this order):**

1. Memory (RAM)
2. Running processes
3. Network connections
4. Open files
5. System logs
6. Disk (full image)

**Use write blockers for disk forensics**

**Document everything with hashes:**

```bash
# Create evidence manifest
sha256sum /path/to/evidence/* > evidence_manifest.txt
```

### Phase 3: Analysis

**Key questions to answer:**

1. **Was the API exposed?**
   - Check firewall rules
   - Review network logs
   - Look for unauthorized IPs

2. **What models were accessed?**
   - Review `ollama list` output
   - Check model file access times
   - Look for unusual model downloads

3. **What prompts were sent?**
   - API request logs (if available)
   - Application logs feeding Ollama
   - Search for suspicious patterns

4. **What data was processed?**
   - Review input data to Ollama
   - Check for sensitive data in prompts
   - Look for PII leakage

5. **What outputs were generated?**
   - Review Ollama responses
   - Check for malicious content generation
   - Look for data exfiltration

### Phase 4: Attribution

**Look for:**

- IP addresses accessing the API
- User accounts used
- Geographic location of attackers
- Tools/methods used (automation, scripts)
- Time patterns (off-hours activity)

---

## 5. Forensic Report Structure

Here's a template for your report:

```markdown
# Ollama Breach Forensic Report

## Executive Summary
- Date of incident
- Systems affected
- Scope of breach
- Key findings

## 1. Background
- What is Ollama
- How it was deployed
- Business context

## 2. Investigation Methodology
- Evidence sources
- Tools used
- Timeline of investigation

## 3. Findings

### 3.1 System Configuration
- Ollama version
- Deployment method
- Network configuration
- Authentication settings

### 3.2 Network Analysis
- Exposed ports
- Firewall rules
- Unauthorized access attempts
- Source IP addresses

### 3.3 API Access Analysis
- Endpoints accessed
- Request volumes
- Unusual patterns
- Sensitive data exposure

### 3.4 Model Analysis
- Models loaded
- Unauthorized model downloads
- Model modification evidence

### 3.5 Log Analysis
- System logs
- Application logs
- Authentication logs
- Error logs

## 4. Evidence Summary
- Evidence collected
- Chain of custody
- Hash values
- Storage locations

## 5. Attack Reconstruction
- Attack timeline
- Attack vector
- Attacker actions
- Data affected

## 6. Impact Assessment
- Data compromised
- Systems affected
- Business impact
- Regulatory implications

## 7. Recommendations
- Immediate remediation
- Security improvements
- Monitoring enhancements
- Policy changes

## 8. Appendices
- Evidence listing
- Log excerpts
- Command outputs
- Screenshots
```

---

## 6. Key Evidence Categories

| Category | What to Look For | Tools |
|----------|------------------|-------|
| **Network** | Unauthorized IPs, unusual traffic volume | Wireshark, tcpdump, logs |
| **System** | Process spawning, file access, timing | Process Monitor, auditd |
| **Application** | API requests, prompts, responses | Ollama logs, app logs |
| **Disk** | Deleted files, model modifications | FTK, EnCase |
| **Memory** | Running malicious prompts, decoded data | Volatility, LiME |

---

## 7. Common Attack Signatures

**Prompt Injection Indicators:**

- Unusual prompt patterns in logs
- System prompts being overridden
- Jailbreak attempts

**Unauthorized Access Indicators:**

- Failed authentication attempts
- Access from unexpected IPs
- Unusual API call volumes

**Data Exfiltration Indicators:**

- Large response payloads
- Unusual query patterns
- Batch requests to sensitive endpoints

---

## 8. Tools for Ollama Forensics

- **Process analysis**: Process Monitor, Process Explorer
- **Network analysis**: Wireshark, tcpdump, Zeek
- **Log analysis**: Splunk, ELK Stack, grep/awk
- **Disk forensics**: FTK Imager, Autopsy
- **Memory forensics**: Volatility Framework
- **Timeline analysis**: Plaso, Timesketch

---

Would you like me to:

1. **Go deeper** on any specific phase?
2. **Create a markdown report template** you can fill in?
3. **Provide specific commands** for a particular OS?
4. **Cover a specific attack scenario** in more detail?
