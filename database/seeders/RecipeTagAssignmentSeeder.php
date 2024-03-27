<?php

namespace Database\Seeders;

use App\Models\Recipe;
use App\Models\Tag;
use Illuminate\Database\Seeder;

class RecipeTagAssignmentSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $recipes = Recipe::all();
        $tags = Tag::all();

        foreach ($recipes as $recipe) {
            foreach ($tags as $tag) {
                $recipe->tags()->attach($tag);
            }
        }
    }
}
