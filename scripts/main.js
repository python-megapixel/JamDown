function showMenu() {
			document.getElementById("side-menu").style = "min-height: 50%;width:50%position: fixed;z-index: 1;top: 0;left: 0;background-color:#FF0000;overflow-x: hidden;padding-top: 20px;";

			var ch = document.getElementById("side-menu").children;
			for (i=2; i<ch.length; i++) {
				ch[i].style = "padding: 6px 8px 6px 16px;width: 100%;text-decoration: none;color: white;display: block;font-size:1em;"
			}

			// document.getElementById("subt1").style.textDecoration = "underline";
			// document.getElementById("subt2").style.textDecoration = "underline";

			// document.getElementById("subt1").style.color = "black";
			// document.getElementById("subt2").style.color = "black";

			document.getElementById("menu-button").style.display = "none";
			document.getElementById("close-button").style.display = "block";
		}

function hideMenu() {
			document.getElementById("side-menu").style = "overflow-y: hidden;";

			var ch = document.getElementById("side-menu").children;
			for (i=0; i<ch.length; i++) {
				ch[i].style = "";
			}

			document.getElementById("menu-button").style.display = "";
			document.getElementById("close-button").style.display = "";
		}
