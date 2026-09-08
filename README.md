# AI 求职助手

这是一个配合 Obsidian 与 Codex 使用的个人求职 Skill。它不只是保存文件，还会基于用户的真实资料完成岗位分析、简历匹配、面试准备、面试复盘和求职进展诊断。

## 能做什么

- 自动建立 Obsidian 求职知识库；
- 整理简历、自我分析和过往经历；
- 用两张 Excel 表记录投递与面试；
- 拆解岗位 JD，寻找有证据的匹配点和材料缺口；
- 针对具体岗位准备面试并进行逐题模拟；
- 从面试转写中整理问题、表现和下一步改进；
- 根据多次投递与面试记录分析当前求职卡点。

## 安装

1. 安装并打开 Obsidian，新建一个用于求职的 Vault。
2. 在 Codex 中把这个 Vault 作为本地项目打开。
3. 将本 GitHub 仓库地址复制给 Codex，并发送：

```text
请使用 skill-installer 安装这个 GitHub Skill：
https://github.com/YFpsy/AI-job-search-assistant.git
```

4. 安装完成后发送：

```text
帮我创建求职知识库。
```

Skill 会自动建立目录、规则文件、索引以及投递和面试工作簿。已有同名文件不会被覆盖。

## 常用说法

- 把这几版简历整理进知识库。
- 我有一段新经历，帮我更新。
- 帮我分析这个岗位是否适合我。
- 帮我根据这个 JD 调整简历。
- 我收到面试了，帮我准备。
- 这是面试转写，帮我复盘。
- 帮我分析最近的投递反馈和下一步。

## 隐私

本仓库只包含 Skill、规则和空白模板，不包含任何用户简历、录音、联系方式或求职记录。个人资料保存在用户自己的 Obsidian Vault 中。

## 文件结构

```text
ai-job-search-assistant/
├─ SKILL.md
├─ agents/openai.yaml
├─ references/
├─ scripts/init_vault.py
└─ assets/vault-template/
```
