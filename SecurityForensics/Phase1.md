# LLM Forensics - Phase 1: Pre-training

---

## Overview

This document covers the pre-training phase of Large Language Models (LLMs), which forms the foundation for all subsequent capabilities. Understanding this phase is 
essential for forensic analysis of LLM behavior, capabilities, and limitations.

---

## 1. Training Data

### 1.1 Data Sources

LLMs are trained on massive, diverse text corpora including:

- Books (fiction and non-fiction)
- Web pages and articles
- Code repositories (GitHub, etc.)
- Wikipedia and encyclopedic content
- Scientific papers
- Social media content
- News articles
- Historical archives

### 1.2 Data Characteristics

**Key characteristics of training data:**

- **Scale**: trillions of tokens
- **Diversity**: multiple languages, domains, formats
- **Quality variance**: includes both high-quality and noisy content
- **Biases**: reflects human biases in source material
- **Temporal coverage**: limited to data available before training cutoff

---

## 2. Training Objective

The primary objective during pre-training is to minimize the loss on next-token prediction. This is known as autoregressive language modeling.

### 2.1 Mathematical Foundation

The model learns to maximize:

**L = Σ log P(w_t | w_1, w_2, ..., w_{t-1})**

Where:

- **w_t** = the t-th token
- **w_1 to w_{t-1}** = previous tokens (context)
- **P** = probability distribution over vocabulary

### 2.2 Tokenization

Before training, text is converted to tokens using:

- Byte Pair Encoding (BPE)
- WordPiece
- SentencePiece

This creates a vocabulary of ~30,000-50,000 tokens.

---

## 3. Model Architecture

### 3.1 Transformer Base

Modern LLMs use the Transformer architecture introduced in "Attention Is All You Need" (2017).

**Key components:**

- Multi-head self-attention
- Feed-forward neural networks
- Layer normalization
- Positional encodings
- Residual connections

### 3.2 Scale

**LLM scale includes:**

- **Parameters**: billions to hundreds of billions
- **Layers**: dozens to hundreds of transformer blocks
- **Attention heads**: dozens per layer
- **Context length**: 1K to 100K+ tokens

---

## 4. Training Process

### 4.1 Optimization

**Training uses:**

- **Optimizer**: AdamW (most common)
- **Learning rate scheduling**: warmup + decay
- **Batch size**: large (thousands to millions of tokens)
- **Mixed precision training**: FP16/BF16
- **Gradient clipping**: to prevent instability

### 4.2 Hardware Requirements

**Pre-training requires massive compute:**

- Thousands of GPUs (A100, H100, etc.)
- Training time: weeks to months
- Estimated cost: millions of dollars for largest models

---

## 5. What the Model Learns

### 5.1 Knowledge Compression

Pre-training compresses information from training data into model weights. The model does not store facts explicitly but learns patterns, relationships, and statistical 
regularities in language.

### 5.2 Capabilities Acquired

After pre-training, models acquire:

- Language understanding and generation
- Grammar and syntax
- Reasoning patterns
- World knowledge (limited by training data)
- Coding abilities
- Cultural and social biases
- Stylistic patterns from training data

### 5.3 Limitations Introduced

**Pre-training introduces fundamental limitations:**

- **Hallucinations**: confident but incorrect outputs
- **Knowledge cutoff**: no awareness of events after training
- **Biases**: reflects training data biases
- **Factual errors**: not a reliable fact database
- **No verification**: cannot check external truth

---

## 6. Forensic Implications

### 6.1 Evidence of Pre-training

Forensic analysts can identify pre-training effects through:

- Memorization of training data (especially for short texts)
- Stylistic patterns from specific domains
- Knowledge boundaries matching training cutoff
- Bias patterns reflecting source data demographics
- Language capabilities matching training corpora

### 6.2 Analysis Methods

**Black-box forensic methods:**

- Probing for specific known facts from training period
- Testing knowledge cutoff dates
- Measuring bias through structured prompts
- Identifying memorization through exact match queries
- Benchmarking on domain-specific tasks

### 6.3 Red-teaming Findings

Red-teaming has revealed that pre-training captures harmful content from the internet, including misinformation, hate speech, and dangerous instructions. This is why 
subsequent fine-tuning phases focus on alignment and safety.

---
