import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { PageNotFoundComponent } from '../components/page-not-found/page-not-found.component';
import { SkeletonCardComponent } from '../components/skeleton-card/skeleton-card.component';
import { DImageFallbackDirective } from '../directives/image-fallback/DImageFallback.directive';
import { PrimengSharedModules } from './primeng-shared.module';

@NgModule({
  imports: [CommonModule, PrimengSharedModules],
  declarations: [
    SkeletonCardComponent,
    PageNotFoundComponent,
    DImageFallbackDirective,
  ],
  exports: [
    DImageFallbackDirective,
    SkeletonCardComponent,

    PageNotFoundComponent,
  ],
})
export class SharedComponentsModule {}
