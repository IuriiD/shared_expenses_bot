# 'SharedExpensesBot' / Chatbot that helps to track shared expenses on the go
<p>
    <b>Try it in <a href="http://t.me/SharedExpensesBot">Telegram</a></b>
    <br>Being built on Dialogflow it can be quite easily ported to other platforms (Facebook Messenger, Skype etc).
</p>
<p>
    <b>The idea</b>
    <br>The idea for this training miniproject was suggested by my <a href="https://www.facebook.com/viktor.dziuban">brother</a> who said that it would be nice to have a chatbot that could help to track shared expenses during travels with friends. For example, when one pays for apartment, someone else for dinner, the 3rd one for gas, some other food/drinks/tickets etc (as an alternative to chipping in with equal sums each time). This idea appeared to be not new but was challenging for me at my level of knowledge at that moment.
</p>
<p>
    <b>How it looks like (Telegram)</b>
    <a href="https://iuriid.github.io/public/img/cbb-5.jpg" target="_blank"><img src="https://iuriid.github.io/public/img/cbb-5.jpg" class="img-fluid img-thumbnail" style="max-width: 800px"></a>
</p>
<p>
    <b>Structure</b>
    <br>Intents structure for SharedExpensesBot is the following:
    <a href="https://iuriid.github.io/public/img/seb_intents_structure.gif" target="_blank"><img src="https://iuriid.github.io/public/img/seb_intents_structure.gif" class="img-fluid img-thumbnail" style="max-width: 800px"></a>
    Bot has 14 functions: welcome, fallback, create/delete log, add/remove user, add/modify/delete payment, show balance/statement, send statement to email and show help). As you can see it uses quite many (17) webhooks. Data is saved in MongoDB.
    <br><a href="https://iuriid.github.io/public/img/seb_db.gif" target="_blank"><img src="https://iuriid.github.io/public/img/seb_db.gif" class="img-fluid img-thumbnail" style="max-width: 800px"></a>
</p>
<p>
    <b>What it can do</b>
    </ul>
        <li>Transactions between users are saved in so called logs. User can have several logs, switch between them, and also delete logs.</li>
        <li>Log creator is automatically added to the list of users and can’t be removed. He can add and delete another users. Users can be added at any stage (at the beginning or after some transactions). Only users with 0 balance can be removed.</li>
        <li>2 types of transactions exist: 1) when somebody pays for all and 2) when one user gives money to another user. Bot understands input like “Tom paid 50 EUR for gas” (also “Tom 50 EUR”), “Dan paid $50 to Mike” (also “Dan $50 Mike”).</li>
        <li>Basic currency is USD. Payments in other currencies are automatically converted to USD using <a href="https://openexchangerates.org/" target="_blank">openexchangerates</a> API.</li>
        <li>Payments can be modified and removed with automatic recalculation of balance.</li>
        <li>Current balance for all or specific user can be displayed. Statement can be displayed and also sent to email.</li>
    </ul>
</p>
<p>
    <b>Possible further improvements</b>
    <ul>
        <li>Function to set custom exchange rates and initial balance</li>
        <li>“Multiplayer” mode: payments can be added by all users in a group (with a system of confirmation of receipt)</li>
        <li>Adding charts to display balance, icons and other fancy features</li>
        <li>Adding charts to display balance, icons and other fancy features</li>
        <li>Porting to Facebook Messenger and other platforms</li>
    </ul>
</p>

