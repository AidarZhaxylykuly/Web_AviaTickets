import {RouterModule, Routes } from '@angular/router'; 
import { AppComponent } from './app.component';
import { SigninComponent } from './signin/signin.component';
import { AviamainComponent } from './aviamain/aviamain.component';
import { SignupComponent } from './signup/signup.component';


export const routes: Routes = [
    {path: '', component: AviamainComponent},
    {path: 'signin', component: SigninComponent},
    {path: 'signup', component: SignupComponent},
];

