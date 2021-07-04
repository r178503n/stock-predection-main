import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { ApplicationSharedModules } from 'src/app/application-shared/modules/application-shared.module';
import { HeaderComponent } from './components/header/header.component';
import { NavigationComponent } from './components/navigation/navigation.component';
import { NavigationRoutingModule } from './navigation-routing.module';

@NgModule({
  imports: [CommonModule, NavigationRoutingModule, ApplicationSharedModules],
  declarations: [NavigationComponent, HeaderComponent],
  exports: [NavigationComponent, HeaderComponent],
})
export class NavigationModule {}
