# Back-End

The overview of this project is creating a hub for people who would like to build a table tennis community in their local area.
As the projects stack rely heavily on the backend, with the team, we took time to focus on the schemas and white boarding, what is the data type, and what is the requirement for every field.
As a start we focused on the schemas to make sure that the infrastructure of the project is quite solid and scalable if ever we need to scale it. Choosing the right technology and assigning tickets for the team members.
Also we have used the MVC to break the backend project into small chunks for clear structure, better understanding and easy distributing among the team member 
The back-end of our project breaks has been divided mainly into three parts with their own schemas and endpoints

# Schemas

This first step is to build the user Schema with the help of mongoose framework to connect to MongoDB as following

## Users

Where the comment Schema nested inside the user schema as well as another schema to demonstrate the relation between schemas using mongoDB.

```Javascript
const userSchema = new mongoose.Schema({
  username: { type: String, required: true, unique: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: [true, 'Password is required'] },
  isAdmin: { type: Boolean },
  //nested schema 
  comments: [commentSchema],
  image: { type: String, required: true },
  bio: { type: String, required: true },
  location: { type: String, required: true }
})

```

Also using npm packages to add layers of security  such as
```Javascript
Import mongooseHidded from ‘mongoose-hidden
Import cbycrypt from ‘bcrypt 
```
Also the same goes with location schema, event schema, comment schema and attendee schema

# Views
The views folder consist of a router file where it contain 14 APIs endpoints with 
14 APIs end point   29 request, either  get, post, update or delete, where those express request connected to the database with help of mongoose 
Also among those APIs user authentication, authorisation and secure routes, example of this 
 
```Javascript
router.route('/user/:id')
 .get(singleUserController.getSingleUser)
 .put(secureRoute, singleUserController.updateSingleUser)
 .delete(secureRoute, singleUserController.deleteSingleUser)
 .post(secureRoute, userComment.createUserComment)

```


# Controllers
Controller folder includes 12 file from attendee to user, single user, login or registration 

## user registration
The aim is to make a friendly experience for the user though the registration process rather make it rigid , so some of the field is not required but some if is crucial  such as, user name, email password. 
Aldo adding an extra feature for registration confirmation by sending an email
back to the user via the email using third party library
For the user registration

```Javascript
const transporter = nodeMailer.createTransport(sendgridTransport({
 auth: {
   api_key: API_KEY
 }
}))
 
async function register(req, res, next) {
 if (req.body.isAdmin) {
   delete req.body.isAdmin
 }
 const body = req.body
 try {
   const user = await User.create(body)
   res.send(
     transporter.sendMail({
       to: body.email,
       from: 'parkpong63@gmail.com',
       subject: 'Registeration successful',
       html: `<h2>Dear ${body.username},</h2> <br><h3> Thank you for your registration with us.</h3>
       <img width="100vw" src="https://images.unsplash.com/photo-1611251126118-b1d4f99600a1?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80"/>
       `
     }))
  
 } catch (err) {
   next(err)
  }
}
 
export default {
 register
}
 
```
 
## User authentication

Using the npm package of json web tike, made the work easy and concise

```Javascript

import jwt from 'jsonwebtoken'
 
async function login(req, res, next) {
 const password = req.body.password
 try {
   const user = await User.findOne({ email: req.body.email })
 
 
   if (!user || !user.validatePassword(password)) {
     return res.status(401).send({ message: 'Unauthorized' })
   
}
 
   const token = jwt.sign(
     { userId: user._id },
     secret,
     { expiresIn: '12h' }
   )
 
   res.status(202).send({ token, message: 'Login successful' })
 } catch (err) {
   next(err)
 }
}
```


## Seeding 
Seeding the database is  with  events data, location data and user data by creating functions and pass some arguments which it makes it easier when seeding for the nested schemas and  referenced ones

```Javascript 
export default function getEventData(users, location) {
 return [
   {
     name: 'Ball Busters',
     location: location[0],
     user: users[0],
     image: 'https://images.unsplash.com/photo-1557804500-7a58fbcd4d1a?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1267&q=80',
     time: ' Sunday 21st March at 3pm',
     details: 'meeting at the south corner of sweet park',
     attendees: [],
     results: [{}],
     comments: []
   },
   {
     name: 'King Pong',
     location: location[1],
     user: users[1],
     image: 'https://images.unsplash.com/photo-1568711146297-b8674c3c11b6?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80',
     time: 'Saturday 20th March at 3pm',
     details: 'meeting at the near pub,  then walking  to the spot ',
     attendees: [],
     results: [{}],
     comments: []
   },

```

## Testing

9 tests run to make sure that there is steady functioning code blocks and making user feature are talking to each other as expected 
The test technology is Mocha and Chai with supertest to test various functionality of the endpoints from deleting to editing and creating, events, locations an dso on

```Javascript

import { expect } from 'chai'
import setup from './lib/setup.js'
import tearDown from './lib/tearDown.js'
 
// * Mocha ☕️
 
describe('Testing GET Event', () => {
 beforeEach(done => {
   setup(done)
 })
 afterEach(done => {
   tearDown(done)
 })
 
 it('should return a 200 response', done => {
   api.get('/api/event')
     .end((err, res) => {
       expect(res.status).to.eq(200)
       done()
     })
 })
```

### Run the web app Locally
To run this web app , simply you have to fork the repository, clone it into your machine and cd to the project-3 folder and run the following command
```Javascript
npm install
npm run serve
```
the web app with run on localhost:8000

Happy haching