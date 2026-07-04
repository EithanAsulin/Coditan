<div align="center">

# Creating custom skills for Coditan
To create skills for Coditan, you must have the following installed:
| **Requirements** | **Version** |
|--------------|---------|
| Coditan      | Latest  |
| Python       |  3.14   |
| GitHub + Git | Latest  |

## A Coditan skill should use the following file structure:
<div>

```files
skill-name/
├── skill.py
├── skill.md
├── icon.png (optional)
├── custom_action.json
├── market.json
├── README.md (optional)
└── extras/ (optional)
```

</div>

## What those files consist of
Here you can read exactly what the custom skills consist of helping you learn how to make your Own.

<details>
<summary>skill.py</summary>

```python
import ...

def skill_name(variables):
    print("In here you can get specific variables and execute actions accordingly")
```
</details>


<details>
<summary>skill.md</summary>

```markdown
# Skill name
{Skill} allows you to do {purpose}, You can trigger it using this format :

<custom_action>
variable_1="var"
variable_2="test"
variable_3="example"
</custom_action>

Variable_1 is used for...
```
</details>

<details>
<summary>custom_action.json</summary>

```json
{
  "skill": {
    "name": "Skill Name",
    "description": "Description of what the skill does",
    "creator": "Creator name",
    "version": "Version",
    "icon": "https://raw.githubusercontent.com/EithanAsulin/Coditan/refs/heads/master/Skill-Name/icon.png",
    "function": "the function in the python script...",
    "path": "The path/folder name",
    "trigger": "trigger_name (must match in the instruction example)",
    "action": "actions/custom/skill-name/skill.py",
    "instructions": "actions/custom/skill-name/skill.md"
  }
}
```
</details>

<details>
<summary>market.json</summary>

```json
{
    "skill": {
        "name": "Skill name",
        "description": "a description matching custom_action.json",
        "creator": "Creator",
        "version": "version",
        "icon": "https://raw.githubusercontent.com/EithanAsulin/Coditan/refs/heads/master/Skill-name/icon.png",
        "json": "https://raw.githubusercontent.com/EithanAsulin/Coditan/refs/heads/master/Skill-name/custom_action.json",
        "script": "https://raw.githubusercontent.com/EithanAsulin/Coditan/refs/heads/master/Skill-name/skill.py",
        "instructions": "https://raw.githubusercontent.com/EithanAsulin/Coditan/refs/heads/master/Skill-name/skill.md",
        "requirements": [
            "Requirements (must be valid for python 3.14)"
        ]
    }
}
```
</details>

## How to test
Once you're done and ready to test all you need to do is navigate in Coditan Like this

```Settings (top right) > Dev Menu > Import custom skill```

One done point it directly to the folder where those files live, it'll read custom_action.json and the requirements from market.json and add the custom skill to the installed skills. Ya 

## How to submit your skill
To submit your skill you must have a valid GitHub account connected to git, when pushing all the skills file must be in a folder with no other files in that directory.

### Step 1 - Clone the latest version of the repository

```bash + git
git clone https://github.com/EithanAsulin/Coditan.git
cd Coditan
```

### Step 2 - Clone the folder

```bash
mv ../Skill-Folder ./
git add ./Skill-Folder
git commit -m "Added custom skill..."
git push -u origin master
```

And that's it you've sucessfully pushed your custom skill into review!
</div>