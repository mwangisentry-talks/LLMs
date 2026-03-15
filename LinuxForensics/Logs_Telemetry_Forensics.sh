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

