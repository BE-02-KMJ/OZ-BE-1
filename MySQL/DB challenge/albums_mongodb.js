db.albums.find({}, {앨범: 1, 연도: 1})
db.albums.find({연도: '2000'})
db.albums.find({최고순위: {$lte: 10}})
db.albums.find({최고순위: '-'})
db.albums.aggregate([{$group: {_id: "$연도", count: {$sum: 1}}}])
db.albums.find().sort({연도: -1}).limit(1)
db.albums.find().sort({연도: 1}).limit(1)
db.albums.find({최고순위: {$gte: 10}})
db.albums.find({앨범: /White/})
db.albums.find({연도: {$gte: '2000', $lte: '2005'}})

// CRUD 연습
db.albums.insert({앨범: 'New Album', 연도: '2024', 최고순위: '1'})

db.albums.update({앨범: 'New Album'}, {$set: {최고순위: '2'}})

db.albums.remove({앨범: 'New Album'})

db.albums.find()