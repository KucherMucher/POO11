import os
import sys
import zipfile
import re

def search_keyword(path, kw, save=False, save_path="."):
    if not kw:
        print("No keyword provided.", file=sys.stderr)
        sys.exit(1)
    try:
        with open(path, encoding='utf-8', errors='ignore') as log:
            found = 0
            for i, line in enumerate(log, 1):
                if kw in line.lower():
                    if save:
                        with open(save_path, "a", encoding="utf-8") as f:
                            f.write(f"\n\n{path}:{i}: {line.rstrip()}")
                    else:
                        print(f"{path}:{i}: {line.rstrip()}")
                    found+=1
        if found == 0:
            if save:
                with open(save_path, "a", encoding="utf-8") as f:
                    f.write("\n")
            else:
                print("No matches.")
    except FileNotFoundError:
        print(f"File not found: {path}", file=sys.stderr)
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)

def search_jar(jar_path, kw, save=False, save_path="."):
    """Search all entries inside a .jar (zip) for a keyword (case-insensitive)."""
    if not kw:
        print("No keyword provided.", file=sys.stderr)
        return
    kwb = kw.encode("utf-8").lower()
    try:
        with zipfile.ZipFile(jar_path, "r") as z:
            for info in z.infolist():
                try:
                    data = z.read(info.filename)
                except Exception:
                    continue
                try:
                    if kwb in data.lower():
                        # attempt to show a printable snippet if available
                        printable = b"".join(re.findall(b"[\\x20-\\x7E]{4,}", data))
                        snippet = ""
                        if printable:
                            try:
                                snippet = printable.decode("utf-8", errors="replace")
                                snippet = snippet[:200] + ("..." if len(snippet) > 200 else "")
                            except Exception:
                                snippet = ""
                        out = f"{jar_path}:{info.filename}: contains keyword"
                        if snippet:
                            out += f" -> {snippet}"
                        if save and save_path:
                            with open(save_path, "a", encoding="utf-8") as f:
                                f.write(out + "\n")
                        else:
                            print(out)
                except Exception:
                    # skip entries we can't process
                    continue
    except zipfile.BadZipFile:
        print(f"Not a valid zip/jar file: {jar_path}", file=sys.stderr)
    except FileNotFoundError:
        print(f"File not found: {jar_path}", file=sys.stderr)
    except Exception as e:
        print(f"Error reading jar {jar_path}: {e}", file=sys.stderr)


save_root = r"C:\Users\snak3\OneDrive\Documents\POO11\my_lil_projects\pyhton_output"
if input("Save in a directory? y/n: ").strip().lower() == 'y':
    filename = input("filename (change path in code): ")
    save = True
    save_path = os.path.join(save_root, f"{filename}.txt")
else:
    save = False
    save_path = "."
    

match int(input("1 - modlist, 2 - find keyword in log, 3 - find keyword in configs: ")):
    case 1:
        filelist = os.listdir(input("Insert file path: "))
        if save:
            with open(save_path, "x", encoding="utf-8") as f:
                f.write("\n".join(filelist))
        else:
            print(filelist)

    case 2:
        path = input("Insert log path: ")
        kw = input("keyword: ").strip().lower()

        search_keyword(path, kw, save, save_path)
        

    case 3:
        path = input("Insert path: ").strip()

        if not path:
            sys.exit(1)
        rec = input("Search subdirectories? y/n: ").strip().lower == 'y'

        kw = input("keyword: ").strip().lower()

        if rec:
            for root, _, files in os.walk(path):
                for name in files:
                    full_path = os.path.join(root, name)
                    if os.path.isfile(full_path):
                        search_keyword(full_path, kw, save, save_path)
        else:
            for name in os.listdir(path):
                full_path = os.path.join(path, name)
                if os.path.isfile(full_path):
                    search_keyword(full_path, kw, save, save_path)

    case 4:
        path = input("Insert folder or jar file path: ").strip()
        if not path:
            sys.exit(1)
        kw = input("keyword: ").strip().lower()
        if not kw:
            print("No keyword provided.", file=sys.stderr)
            sys.exit(1)
        rec = input("Search subdirectories? y/n: ").strip().lower() == 'y'

        # single jar file
        if os.path.isfile(path) and path.lower().endswith(".jar"):
            search_jar(path, kw, save, save_path)
        else:
            # folder: find .jar files and search them
            if rec:
                for root, _, files in os.walk(path):
                    for name in files:
                        if name.lower().endswith(".jar"):
                            full_path = os.path.join(root, name)
                            if os.path.isfile(full_path):
                                search_jar(full_path, kw, save, save_path)
            else:
                for name in os.listdir(path):
                    if name.lower().endswith(".jar"):
                        full_path = os.path.join(path, name)
                        if os.path.isfile(full_path):
                            search_jar(full_path, kw, save, save_path)

        
