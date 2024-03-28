<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Comment;
use Illuminate\Database\Eloquent\ModelNotFoundException;
use Exception;


class CommentController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        return Comment::all();
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        //
    }


    public function store(Request $request)
    {
        try{
            $validated_data = $request->validate([
                'comment' => 'required|string',
                
            ]);
            Comment::create($validated_data);
            return response()->json([
                'message' => 'Comment added successfully'
            ], 201);
        } catch (Exception $e){
            return response()->json(['message' => 'error', 'error' => $e->getMessage()], 500);
        }
    }
    
    public function show($id)
    {
        $comment = Comment::find($id);
        if (!$comment){
            return response()->json(['message' => 'Comment not found'], 404);
        }
        return response()->json(['comment' => $comment], 200);
    }


    public function edit(string $id)
    {
        // Get the comment by its id and pass it to the view
        // return View('comments.edit')->withComment(Comment::find($id));
    }

    
    public function update(Request $request, $id)
    {
        // $comment = Comment::findOrFail($id);
        // $comment->update($request->all());
        // return response()->json($comment, 200);
        try{
            $comment = Comment::findOrFail($id);
            return response()->json($comment, 200);
        }catch (ModelNotFoundException $e){
            return response()->json(['message' => 'Comment not found'], 404);
        } catch (Exception $e) {
            return response()->json(['message' => 'error', 'error' => $e->getMessage()], 500);
        }
    }

    
    public function destroy($id)
    {
        // $comment = Comment::findOrFail($id);
        // $comment->delete();
        // return response()->json(null, 204);
        try{
            $comment = Comment::findOrFail($id);
            $comment->delete();
            return response()->json(null, 204);
        }catch(ModelNotFoundException $e){
            return response()->json(null, 404);
        }
    }
}
