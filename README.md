# algorithm-python

经典算法的 Python 实现与学习仓库，涵盖排序、查找等基础算法，并附带机器学习示例。
目标是让每个实现都有配套的说明、使用示例与复杂度/原理分析。

> **当前状态**：项目处于起步阶段。已落地的是 `src/ml` 包（基于 scikit-learn 的 KNN 演示程序）以及完整的工程化配置（构建、测试、lint、CI）；排序、查找算法模块和真正的单元测试尚未提交。详见文末「当前状态与待完善」。

## 项目概览

| 项目 | 内容 |
| --- | --- |
| 分发名称 | `algorithm-python` |
| 版本 | `0.1.0` |
| 导入包名 | `ml`（源码位于 `src/ml`） |
| 作者 | Chuanfei Wang |
| 许可证 | MIT |
| Python 要求 | `>= 3.10`（本地开发环境为 3.13） |
| 运行时依赖 | `scikit-learn >= 1.9` |
| 开发依赖 | `pytest`、`black`、`ruff`、`mypy` |

## 目录结构

```text
algorithm-python/
├── .github/workflows/ci.yml    # GitHub Actions 持续集成（Python 3.10 ~ 3.13）
├── src/ml/                     # 源码包（src 布局）
│   ├── __init__.py             # 包入口，提供 __version__
│   └── __main__.py             # 命令行演示：python -m ml
├── tests/                      # 测试套件（目前仅有 __init__.py）
│   └── __init__.py
├── docs/                       # 文档（index.md 为占位）
│   └── index.md
├── requirements/               # 依赖声明
│   ├── requirements.txt        # 运行时依赖：scikit-learn >= 1.9
│   └── requirements-ml.txt     # 固定版本依赖：scikit-learn==1.9.1 + -e .
├── pyproject.toml              # 项目元数据、依赖与工具配置
├── Makefile                    # 常用命令（install/dev/test/lint/format/clean）
├── LICENSE                     # MIT 许可证
└── README.md                   # 本文件
```

项目采用 **src 布局**：源码与测试/文档分离，避免开发时误导入未安装的包。测试通过 `pyproject.toml` 中的 `pythonpath = ["src"]` 找到源码。

## 快速开始

### 1. 创建虚拟环境

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
```

### 2. 安装依赖

```bash
# 安装项目本身（可编辑模式）
python3 -m pip install -e .

# 安装运行时依赖（scikit-learn）
python3 -m pip install -r requirements/requirements.txt
```

如需固定版本的运行环境，可使用：

```bash
python3 -m pip install -r requirements/requirements-ml.txt
```

### 3. 安装开发依赖（测试 / lint / 格式化）

开发依赖定义在 `pyproject.toml` 的 `[project.optional-dependencies] dev` 中：

```bash
python3 -m pip install -e ".[dev]"
```

## 使用示例

### 命令行演示

`src/ml/__main__.py` 提供了一个固定数据集上的 KNN 演示：使用 `KNeighborsRegressor` 做回归预测，再用 `KNeighborsClassifier` 做分类预测。

```bash
python -m ml
```

示例输出：

```text
[3.25]
[3]
```

### 作为库导入

```python
import ml

print(ml.__version__)   # 0.1.0
```

> 说明：当前 `python -m ml` 不接受命令行参数，演示使用代码内固定的训练/测试数据。排序算法、查找算法等 Python API 仍在规划中。

## 测试与代码规范

```bash
make test        # 运行 pytest
make lint        # ruff 检查 + mypy 严格类型检查
make format      # black 格式化 + ruff 自动修复
make clean       # 清理缓存与构建产物
```

需要先安装开发依赖（见上文）。相关工具配置位于 `pyproject.toml`：

- **pytest**：`testpaths = ["tests"]`，`pythonpath = ["src"]`
- **black**：行宽 88，目标版本 py310
- **ruff**：行宽 88，启用规则 `E, F, I, UP, B, SIM`
- **mypy**：`strict = true`，检查范围 `src`

## 持续集成

`.github/workflows/ci.yml` 配置了 GitHub Actions：在 `main` 分支的 push 和 pull request 上触发，使用 Python 3.10 / 3.11 / 3.12 / 3.13 矩阵依次执行 lint（ruff + mypy）与测试（pytest）。

## 当前状态与待完善

以下为仓库当前的实际状态与已知不一致之处，便于后续维护：

1. **包名与分发名不一致**：分发名是 `algorithm-python`，但导入包名是 `ml`。`pyproject.toml` 中的控制台脚本 `algorithm-python = "algorithm_python.__main__:main"` 目前与源码不匹配（不存在 `algorithm_python` 包，也没有 `main()` 函数）；可用的入口是 `python -m ml`。
2. **开发依赖文件缺失**：`Makefile` 的 `dev` 目标和 CI 引用了 `requirements/requirements-dev.txt`，但该文件尚未创建。请改用 `pip install -e ".[dev]"` 安装开发依赖。
3. **测试尚未落地**：`tests/` 目前只有 `__init__.py`，没有实际测试用例（`pyproject.toml` 的 `[dev]` 已包含 pytest）。编译缓存中曾出现 `test_sorting`、`test_searching`，但对应源码文件已不在仓库中。
4. **文档待补充**：`docs/index.md` 目前仅有标题占位。
5. **规划中的模块**：排序（`sorting/`）、查找（`searching/`）算法与 `examples/` 使用示例尚未实现，README 早期版本曾描述这些结构，作为后续开发目标保留。

## 许可证

[MIT](LICENSE) © 2026 Chuanfei Wang
