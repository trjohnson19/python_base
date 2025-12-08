#!/usr/bin/env python3

import tomllib
import pathlib

# Get the desired python project name
def get_author_name_new() -> str:
	return input("Enter the author's (user)name: ")

def get_author_email_new() -> str:
	return input("Enter the author's email: ")

def get_project_name_new() -> str:
	return input("Enter the desired name of the project: ")

def get_project_description_new() -> str:
	return input("Enter the desired project description: ")

def update_pyproject(
		pyproject_path: pathlib.Path,
		project_name_old: str,
		project_name_new: str,
		project_description_old: str,
		project_description_new: str,
		author_name_old: str,
		author_name_new: str,
		author_email_old: str,
		author_email_new: str
		) -> None:
	pyproject_current = tomllib.loads(pyproject_path.read_text())

	project = pyproject_current.get("project", {})
	if project["name"] == project_name_old:
		project["name"] = project_name_new
	if project["description"] == project_description_old:
		project["description"] = project_name_new
	authors = project.get("authors", [])
	for author in authors:
		if author["name"] == author_name_old:
			author["name"] = author_name_new
		if author["email"] == author_email_old:
			author["email"] = author_email_new

	scripts = pyproject_current.get("scripts", {})
	if project_name_old in scripts:
		scripts[project_name_new] = project_name_new + ":main"

	def toml_dump(d: dict[dict[str, str] | str, str], indent: int=0) -> str:
		lines: list[str] = []
		for k, v in d.items():
			if isinstance(v, dict):
				# section header, e.g. [project] or [project.scripts]
				header = f'{"[" * (indent + 1)}{k}{"]" * (indent + 1)}'
				lines.append("\n" + header)
				lines.append(toml_dump(v, indent + 1))
			elif isinstance(v, list):
				# list of tables (authors) or simple lists
				if v and isinstance(v[0], dict):
					# list of tables – each entry on its own line
					lines.append(f"{k} = [")
					for item in v:
						inner = ", ".join(
							f'{ik} = "{iv}"' if isinstance(iv, str) else f"{ik} = {iv}"
							for ik, iv in item.items()
						)
						lines.append(f"  {{ {inner} }},")
					lines.append("]")
				else:
					list_repr = "[" + ", ".join(repr(item) for item in v) + "]"
					lines.append(f"{k} = {list_repr}")
			else:
				# scalar value
				val_repr = f'"{v}"' if isinstance(v, str) else repr(v)
				lines.append(f"{k} = {val_repr}")
		return "\n".join(lines)

if __name__ == "__main__":
	project_name_old: str = "python_base"
	project_name_new: str = get_project_name_new()

	project_description_old: str = \
		"`python_base`: a fully featured `uv` base repo for python development"
	project_description_new: str = get_project_description_new()

	author_name_old: str = "trjohnson19"
	author_name_new: str = get_author_email_new()

	author_email_old: str = "77356759+trjohnson19@users.noreply.github.com"
	author_email_new: str = get_author_email_new()

	base_dir: pathlib.Path = pathlib.Path(__file__).parent
	path_old: pathlib.Path = base_dir.joinpath(
		"src",
		project_name_old
	)
	path_new: pathlib.Path = base_dir.joinpath(
		"src",
		project_name_new
	)
	path_old.move(path_new)

	path_pyproject: pathlib.Path = base_dir.joinpath("pyproject.toml")

	update_pyproject(
		path_pyproject,
		project_name_old,
		project_name_new,
		project_description_old,
		project_description_new,
		author_name_old,
		author_name_new,
		author_email_old,
		author_email_new,
	)

	# try:
	# 	rename_from = base_dir + os.pathsep + "src" + os.pathsep + project_name_old
	# 	rename_to = base_dir + os.pathsep + "src" + os.pathsep + project_name_new
	# 	os.rename(
	# 		rename_from,
	# 		rename_to
	# 	)
	# except PermissionError:
	# 	print("Permission error")
