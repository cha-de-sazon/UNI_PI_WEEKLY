vp = int(input())
fn = int(input())
fp = int(input())
vn = int(input())

acc = float()
pre = float()
sen = float()

acc = (vp + vn) / (vp + vn + fp + fn)
pre = vp / (vp + fp)
sen = vp / (vp + fn)

print(f"{acc:.2}")
print(f"{pre:.2}")
print(f"{sen:.2}")