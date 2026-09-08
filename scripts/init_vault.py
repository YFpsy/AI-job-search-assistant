#!/usr/bin/env python3
"""Initialize the AI job-search Obsidian Vault without overwriting files."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


DIRECTORIES = (
    "00_个人资料/自我分析",
    "00_个人资料/过往经历",
    "00_个人资料/简历版本",
    "01_求职过程/岗位档案",
    "02_外部参考/行业观察",
    "02_外部参考/求职方法",
)

TEXT_TEMPLATES = {
    "AGENTS.md": "AGENTS.md",
    "_知识库索引.md": "_知识库索引.md",
    "_当前求职状态.md": "_当前求职状态.md",
    "00_个人资料/个人档案.md": "个人档案.md",
}

WORKBOOK_TEMPLATES = {
    "01_求职过程/投递记录.xlsx": "投递记录.xlsx",
    "01_求职过程/面试记录.xlsx": "面试记录.xlsx",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--vault", required=True, help="Obsidian Vault root")
    return parser.parse_args()


def validate_vault(path: Path) -> Path:
    resolved = path.expanduser().resolve()
    anchor = Path(resolved.anchor)
    if resolved == anchor or resolved == Path.home().resolve():
        raise ValueError("拒绝在磁盘根目录或用户主目录初始化")
    if not resolved.exists() or not resolved.is_dir():
        raise ValueError("Vault 路径必须是已经存在的文件夹")
    return resolved


def copy_if_missing(source: Path, destination: Path, created: list[str], skipped: list[str]) -> None:
    if destination.exists():
        skipped.append(str(destination))
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    created.append(str(destination))


def main() -> None:
    args = parse_args()
    vault = validate_vault(Path(args.vault))
    skill_root = Path(__file__).resolve().parent.parent
    assets = skill_root / "assets" / "vault-template"
    created: list[str] = []
    skipped: list[str] = []

    for relative in DIRECTORIES:
        target = vault / relative
        if target.exists():
            skipped.append(str(target))
        else:
            target.mkdir(parents=True, exist_ok=False)
            created.append(str(target))

    for destination, source in TEXT_TEMPLATES.items():
        copy_if_missing(assets / source, vault / destination, created, skipped)

    for destination, source in WORKBOOK_TEMPLATES.items():
        copy_if_missing(assets / source, vault / destination, created, skipped)

    print(json.dumps({"vault": str(vault), "created": created, "skipped": skipped}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
