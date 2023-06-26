from flet import *

def main(page:Page):
	page.window_width=400
	page.padding = 0
	page.spacing = 0
	page.bgcolor ="blue200"

	# AND CREATE BULET FOR RIGHT AND LEFT POSITION
	bullet = Container(

		# AND FOR RIGHT AND LEFT SET OFFSET FOR BULLET
		offset=transform.Offset(0,0),
		# AND SET FOR ANIMATION
		animate_offset=animation.Animation(200,"easeIn"),
		shape=BoxShape.CIRCLE,
		bgcolor="blue200",
		height=90,
		left=1,
		right=1,
		margin=margin.only(
			top=page.window_height-80
			),
		content=Icon(name="bookmark",size=40)
		)

	def changeposition(e):
		if e.control.data == "home":
			bullet.offset = transform.Offset(-0.4,0)
			# AND CHANGE ICON 
			bullet.content = Icon(name="home",size=40)
			page.bgcolor="yellow"
			bullet.bgcolor="yellow"
		if e.control.data == "bookmark":
			bullet.offset = transform.Offset(0.0,0)
			# AND CHANGE ICON 
			bullet.content = Icon(name="bookmark",size=40)
			page.bgcolor="blue200"
			bullet.bgcolor="blue200"
		if e.control.data == "person":
			bullet.offset = transform.Offset(0.4,0)
			# AND CHANGE ICON 
			bullet.content = Icon(name="person",size=40)
			page.bgcolor="red200"
			bullet.bgcolor="red200"
		page.update()







	# NOW CREATE NAV IN BOTTOM YOU APP
	nav = Container(
		bgcolor="white",
		width = page.window_width,
		# AND SET THIS TO BOTTOM
		margin=margin.only(
			top=page.window_height-60
			),
		border_radius=30,
		content=Row([
			IconButton(icon="home",
				icon_size=40,
				data="home",
				on_click=changeposition
				),
			IconButton(icon="bookmark",
				icon_size=40,
				data="bookmark",
				on_click=changeposition
				),
			IconButton(icon="person",
				icon_size=40,
				data="person",
				on_click=changeposition
				),
			],alignment="spaceBetween")
		)

	page.add(
		Stack([
			nav,
			bullet,
			])
		)


flet.app(target=main)
