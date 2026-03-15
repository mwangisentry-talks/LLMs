# Basic Linux log forensics you can start today

# Check authentication logs
cat /var/log/auth.log

# Check system logs
journalctl -xe

# Find recently modified files
find / -mtime -1 -type f 2>/dev/null

# Check who's logged in / was logged in
last
lastlog
who

# Check running processes
ps aux
top / htop

# Network connections
ss -tulnp
netstat -anp
```

These are real forensic commands investigators use daily.

---

### 6. Learning Resources (All Free)

- **SANS Reading Room** — free forensic whitepapers
- **13Cubed YouTube channel** — excellent forensics tutorials
- **The Sleuth Kit & Autopsy docs** — hands on
- **Volatility Foundation docs** — for memory forensics
- **OpenSecurityTraining2.org** — deep technical courses, free

---

### Suggested Learning Path
```
Week 1-2:   Learn Autopsy + image a USB drive and analyze it
Week 3-4:   Try Volatility on a memory dump from Digital Corpora
Week 5-6:   Do your first CTF forensics challenge on TryHackMe
Month 2+:   Pick a specialization — network, memory, or malware