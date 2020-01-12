from firebase import firebase
firebase = firebase.FirebaseApplication('https://support-xoohxc.firebaseio.com/', None)
result = firebase.get('data', None)
print(result)