css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.a5rem; margin-bottom: 1rem; display: flex
}
.chat-message .user {
    background-color: #2b313e
}
.chat-message .avatar {
    with: 15%
}
.chat-message .avatar img {
    max-width: 78px;
    max-height: 78px;
    border-radius: 50%;
    object-fit: cover;
}
.chat-message .message {
    width: 85%;
    padding: 0 1.5rem;
    color: #807E7E;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src='https://i.ibb.co/qWBwpNb/Photo-logo-5.png'>
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
         <img src='https://i.ibb.co/DtP1r3p/output-onlinepngtools.png'>
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
