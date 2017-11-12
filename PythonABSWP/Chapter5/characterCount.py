message = 'It is a very cold weather today, does not feel like going outside.'
count={}

for character in message:
	count.setdefault(character, 0)
	count[character]=count[character]+1;

print(count)
