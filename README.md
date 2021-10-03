numbering2pdf adds numbering to pdf file

Example:

```python
from numbering2pdf import add_numbering_to_pdf

add_numbering_to_pdf("old_file.pdf", "new_file.pdf")
```

Parameters:

pdf_file - string or bytes

```python
add_numbering_to_pdf("old_file.pdf", "new_file.pdf")
```

```python
file = open("new.pdf", "br")
read_file = file.read()
file.close()
add_numbering_to_pdf(read_file, "new_file.pdf")
```

```python
new_file = add_numbering_to_pdf("old_file.pdf")
```

---

new_pdf_file_path - path to new pdf file

```python
add_numbering_to_pdf("old_file.pdf", "test/new_file.pdf")
```

---

position - position on screen (left, center, right)

```python
add_numbering_to_pdf("old_file.pdf", "old_file.pdf", position="left")
```

```python
add_numbering_to_pdf("old_file.pdf", "old_file.pdf", position="center")
```

```python
add_numbering_to_pdf("old_file.pdf", "old_file.pdf", position="right")
```

---

start_page - from which page number will the numbering be added

```python
add_numbering_to_pdf("old_file.pdf", "old_file.pdf", start_page=3)
```

---
end_page - on which page number will the numbering be completed

```python
add_numbering_to_pdf("old_file.pdf", "old_file.pdf", end_page=10)
```

---
start_index - which number will the page numbering start from

```python
add_numbering_to_pdf("old_file.pdf", "old_file.pdf", start_index=4)
```

---
size - number size

```python
add_numbering_to_pdf("old_file.pdf", "old_file.pdf", size=25)
```

---
font - font type

Courier, Courier-Bold, Courier-Oblique, Courier-BoldOblique,
Helvetica, Helvetica-Bold, Helvetica-Oblique, Helvetica-BoldOblique,
Times-Roman, Times-Bold, Times-Italic, Times-BoldItalic,
Symbol, ZapfDingbats

```python
add_numbering_to_pdf("old_file.pdf", "old_file.pdf", font="Courier")
```