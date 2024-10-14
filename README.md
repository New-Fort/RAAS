# Rasz API
A free REST API (RAAS- Rasz As A Service) serving quotes from **Mr. Rasz** ❤️

Built with **Flask**, hosted on [PythonAnywhere](https://eu.pythonanywhere.com)

## Usage
**GET https://newfortie.eu.pythonanywhere.com/**
```
To get a quote, use /get-quote
```

**GET https://newfortie.eu.pythonanywhere.com/get-quote**
```
{
    "quote": "To nic. Od wody się nie umiera."
}
```

**GET https://newfortie.eu.pythonanywhere.com/get-quote?key=kita**

*Returns only quotes with the specified key as a substring. Not case sensitive*
```
{
    "quote": "Kita. Last call."
}
```

## License
GPL-3.0 license
