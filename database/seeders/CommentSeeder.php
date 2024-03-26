<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use App\Models\Recipe;
use App\Models\User;

class CommentSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $recipes = Recipe::all();
        foreach($recipes as $recipe){
            for($i=0; $i<5;$i++){
                $user = User::all()->random();
                $comment = $recipe->comments()->make(['comment' => fake()->sentence(5) ]);
                $comment->comment_author()->associate($user);
                $comment->save();
                // $comment->comments()->make(['comment' => fake()->sentence()])->associate($user)->save();
                $new_comment = $comment->comments()->make(['comment' => fake()->sentence(5)]);
                $new_comment->comment_author()->associate($user);                
                $new_comment->save();
            }


        }

    }
}
