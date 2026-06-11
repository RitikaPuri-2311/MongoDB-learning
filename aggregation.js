// Users by role

db.users.aggregate([
    {
        $group: {
            _id: "$role",
            totalUsers: { $sum: 1 }
        }
    }
])

// Users by city

db.users.aggregate([
    {
        $group: {
            _id: "$address.city",
            totalUsers: { $sum: 1 }
        }
    }
])

// Skill distribution

db.users.aggregate([
    { $unwind: "$skills" },
    {
        $group: {
            _id: "$skills",
            count: { $sum: 1 }
        }
    },
    {
        $sort: {
            count: -1
        }
    }
])

// Average age by role

db.users.aggregate([
    {
        $group: {
            _id: "$role",
            averageAge: { $avg: "$age" }
        }
    }
])

// Top skilled users

db.users.aggregate([
    {
        $project: {
            name: 1,
            skillCount: { $size: "$skills" }
        }
    },
    {
        $sort: {
            skillCount: -1
        }
    }
])